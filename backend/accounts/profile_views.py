from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView

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


@login_required
def logout_view(request):
    logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    return redirect('homepage')
