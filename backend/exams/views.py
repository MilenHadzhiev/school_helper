from os.path import join

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView

from exams.models import Exam
from questions.models import Question, Answer
from results.models import Result
from results.views import exam_result


class ExamCreate(CreateView):
    pass


class ExamList(ListView):
    model = Exam
    template_name = 'exams/exam_list.html'


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
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        print(data_)
        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        exam = Exam.objects.get(pk=pk)
        score = 0
        multiplier = 100 / len(exam.get_questions())
        results = []
        correct_answer = None

        for q in questions:
            answer_selected = data_.get(str(q))[0]

            if answer_selected != '':
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if answer_selected == a.text:
                        if a.correct_answer:
                            score += 1
                            correct_answer = a.text
                            break
                    else:
                        if a.correct_answer:
                            correct_answer = a.text
                            break
                results.append(
                    {str(q): {
                        'correct': correct_answer,
                        'selected': answer_selected
                    }}
                )
            else:
                results.append({str(q): 'Не е отговорен'})

        score_ = score * multiplier
        result = Result.objects.create(exam=exam, user=user, score=score_)

        if score_ >= exam.required_score_to_pass:
            url = 'http://' + request.get_host()
            redirect_url = join(url, 'exams', 'results', str(result.id))
            return JsonResponse(
                {'passed': True,
                 'score': score_,
                 'results': results,
                 'redirect_url': redirect_url})
        else:
            url = 'http://' + request.get_host()
            redirect_url = join(url, 'exams', 'results', str(result.id))
            return JsonResponse(
                {'passed': True,
                 'score': score_,
                 'results': results,
                 'redirect_url': redirect_url})
