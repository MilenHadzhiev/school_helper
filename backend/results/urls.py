from django.urls import path

from results.views import exam_result

urlpatterns = [
    path('<int:pk>/', exam_result, name='exam result'),
]
