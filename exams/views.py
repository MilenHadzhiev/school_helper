from os.path import join

from django.http import JsonResponse
from django.shortcuts import render

from django.views.generic import ListView, CreateView, DetailView

from exams.models import Exam
from questions.models import Question
from results.models import Result


class ExamCreate(CreateView):
    pass


class ExamList(ListView):
    model = Exam
    template_name = 'exams/exam_list.html'


# class ExamView(DetailView):
#     model = Exam
#     template_name = 'exams/exam.html'


def exam_view(request, pk):
    exam = Exam.objects.get(pk=pk)
    context = {
        'exam': exam,
    }
    return render(request, 'exams/exam.html', context)


def exam_data_view(request, pk):
    exam = Exam.objects.get(pk=pk)
    questions = []

    for question in exam.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append(answer.text)
        questions.append(
            {str(question): answers}
        )

    return JsonResponse(
        {'data': questions}
    )


def exam_save_view(request, pk):
    if request.is_ajax():
        questions = []  # processing the input information
        data = request.POST  # after the user has submitted the exam
        data_ = dict(data.lists())  # converting the querydict into normal dict
        data_.pop('csrfmiddlewaretoken')  # removing the csrf token; only question-answer pairs are left in data_

        user = request.user
        exam = Exam.objects.get(pk=pk)
        score = 0
        multiplier = 100 / len(exam.get_questions())
        results = []
        correct_answer = None

        for (q, a) in data_.items():  # iterating through the question-answer pairs
            if a[0] != '':  # a is a list of answers containing one string
                question = Question.objects.get(text=q)
                question_answers = question.get_answers()  # getting all answers tied to this question object
                for answer in question_answers:
                    if a[0] == answer.text:  # checking if the answer selected by the user is the correct one
                        if answer.correct_answer:  # a[0] is the answer selected by the user
                            score += 1  # answer is one of the possible answers
                            correct_answer = answer.text
                            break
                    else:
                        if answer.correct_answer:
                            correct_answer = answer.text
                            break

                results.append(
                    {q: {
                        'correct': correct_answer,
                        'selected': a[0]
                    }
                    }
                )
            else:
                results.append({q: 'Не е отговорен'})

        score_ = round(score * multiplier, 2)
        result = Result.objects.create(exam=exam, user=user, score=score_)

        grade = 2
        if score_ > exam.required_score_to_pass:
            grade = 3
        if score_ > exam.required_score_four:
            grade = 4
        if score_ > exam.required_score_five:
            grade = 5
        if score_ > exam.required_score_six:
            grade = 6

        if score_ >= exam.required_score_to_pass:
            url = 'http://' + request.get_host()
            redirect_url = join(url, 'exams', 'results', str(result.id))
            return JsonResponse(
                {'passed': True,
                 'score': score_,
                 'results': results,
                 'grade': grade,
                 'redirect_url': redirect_url})
        else:
            url = 'http://' + request.get_host()
            redirect_url = join(url, 'exams', 'results', str(result.id))
            return JsonResponse(
                {'passed': False,
                 'score': score_,
                 'results': results,
                 'grade': grade,
                 'redirect_url': redirect_url}
            )
