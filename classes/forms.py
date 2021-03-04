from django import forms

from classes.models import Lesson


class LessonCreateForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ('teacher',)
