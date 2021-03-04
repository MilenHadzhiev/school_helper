from django.urls import path, include

from exams.views import ExamList, exam_view, exam_data_view, exam_save_view

app_name = 'exams'


def result_view(args):
    pass


urlpatterns = [
    path('', ExamList.as_view(), name='exams list'),
    path('<int:pk>/', exam_view, name='exam detail'),
    path('<int:pk>/save/', exam_save_view, name='exam save'),
    path('<int:pk>/data/', exam_data_view, name='exam data'),
    path('results/', include('results.urls')),
]
