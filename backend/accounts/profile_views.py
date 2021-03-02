from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from accounts.forms import ProfileEditForm
from accounts.models import User


class ProfileUser(LoginRequiredMixin, DetailView):
    template_name = 'accounts/user_profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        context['current_user'] = user
        context['has_edit_link'] = pk is None
        context['is_teacher'] = user.is_teacher
        if user.is_teacher:
            context['lessons'] = user.lesson_set.all()
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)


class ProfileUserEdit(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/user_profile_edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('current profile')
    model = User

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['email'] = user.email
        initial['profile_picture'] = user.profile_picture
        initial['school'] = user.school
        return initial

    def form_valid(self, form):
        self.object = form.save()
        self.object.profile_picture = form.cleaned_data['profile_picture']
        self.object.school = form.cleaned_data['school']
        self.object.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)


@login_required
def logout_view(request):
    logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    return redirect('homepage')
