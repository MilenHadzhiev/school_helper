from django.shortcuts import render


# Create your views here.
from results.models import Result


def exam_result(request, pk):
    result_exam = Result.objects.get(pk=pk)
    grade = None
    if result_exam.score >= result_exam.exam.required_score_six:
        grade = 'Отличен 6'
    elif result_exam.score >= result_exam.exam.required_score_five:
        grade = 'Много добър 5'
    elif result_exam.score >= result_exam.exam.required_score_four:
        grade = 'Добър 4'
    elif result_exam.score >= result_exam.exam.required_score_to_pass:
        grade = 'Среден 3'
    else:
        grade = 'Слаб 2'

    context = {
        'exam_result': result_exam,
        'grade': grade
    }
    return render(request, 'exams/result.html', context)
