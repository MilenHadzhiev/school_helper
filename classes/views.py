from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from accounts.models import User
from classes.forms import LessonCreateForm
from classes.models import Lesson


class CreateLessonView(LoginRequiredMixin, CreateView):
    form_class = LessonCreateForm
    template_name = 'lessons/lesson_create.html'
    success_url = reverse_lazy('current user lessons')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.teacher = self.request.user
        self.object.save()
        return super().form_valid(form)


class LessonPage(LoginRequiredMixin, DetailView):
    template_name = 'lessons/lesson_detail.html'
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['lesson'] = Lesson.objects.get(pk=pk)
        context['can_change'] = self.request.user == context['lesson'].teacher
        return context


class LessonsUser(ListView):
    template_name = 'lessons/lessons_list.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user = self.request.user if pk is None else User.objects.get(pk=pk)
        self.queryset = user.lesson_set.all()
        return self.queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.get_queryset()
        return context


class LessonsList(ListView):
    template_name = 'lessons/lessons_list.html'

    def get_queryset(self):
        self.queryset = Lesson.objects.all()
        return self.queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.get_queryset()
        context['is_user_lessons_page'] = False
        return context


class LessonEdit(LoginRequiredMixin, UpdateView):
    template_name = 'lessons/lesson_edit.html'
    model = Lesson
    form_class = LessonCreateForm

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        if request.user != Lesson.objects.get(pk=pk).teacher:
            return render(request, 'permission_denied.html')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy(
            'lesson detail',
            kwargs={'pk': pk}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['lesson'] = Lesson.objects.get(pk=pk)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class LessonDelete(LoginRequiredMixin, DeleteView):
    template_name = 'lessons/lesson_delete.html'
    model = Lesson
    success_url = reverse_lazy('current user lessons')
