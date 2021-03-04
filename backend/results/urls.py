from django.urls import path

from results.views import exam_result, UserResultsList

urlpatterns = [
    path('', UserResultsList.as_view(), name='user exam results'),
    path('<int:pk>/', exam_result, name='exam result'),
]
