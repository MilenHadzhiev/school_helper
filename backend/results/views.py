from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

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
    return render(request, 'results/result.html', context)


class UserResultsList(ListView):
    template_name = 'results/user_results_list.html'
    context_object_name = 'results'

    def get_queryset(self):
        self.queryset = self.request.user.result_set.all()
        x = 5
        return self.queryset
