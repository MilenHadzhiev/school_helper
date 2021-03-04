from django import forms

from questions.models import Question


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',)
