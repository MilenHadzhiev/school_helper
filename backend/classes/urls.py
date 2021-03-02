from django.urls import path

from classes.views import LessonsList, LessonPage, LessonsUser, CreateLessonView, LessonEdit, LessonDelete

urlpatterns = [
    path('create/', CreateLessonView.as_view(), name='create lesson'),
    path('<int:pk>/', LessonPage.as_view(), name='lesson detail'),
    path('all/', LessonsList.as_view(), name='lessons list'),
    path('all/user/', LessonsUser.as_view(), name='current user lessons'),
    path('all/user/<int:pk>/', LessonsUser.as_view(), name='user lessons'),
    path('edit/<int:pk>/', LessonEdit.as_view(), name='edit lesson'),
    path('delete/<int:pk>/', LessonDelete.as_view(), name='delete lesson'),
]
