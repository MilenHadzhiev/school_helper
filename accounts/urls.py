from django.urls import path, include

from accounts.views.students import StudentSignUpView
from accounts.views.teachers import TeacherSignUpView
from accounts.profile_views import ProfileUser, logout_view, ProfileUserEdit

urlpatterns = [
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('profile/edit/', ProfileUserEdit.as_view(), name='edit profile'),
    path('profile/', ProfileUser.as_view(), name='current profile'),
    path('profile/<int:pk>/', ProfileUser.as_view(), name='user profile'),
    path('logout/', logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
]
