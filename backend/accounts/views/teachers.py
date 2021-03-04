from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.views.generic import CreateView

from accounts.forms import TeacherSignUpForm
from accounts.models import User


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/teacher_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user.school = form.cleaned_data.get('school')
        user.save()
        teachers_group = Group.objects.get(name='Teachers')
        teachers_group.user_set.add(user)
        login(self.request, user)
        return redirect('homepage')
