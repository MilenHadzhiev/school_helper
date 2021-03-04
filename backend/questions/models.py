from django.db import models

# Create your models here.
from exams.models import Exam


class Question(models.Model):
    text = models.CharField(max_length=200)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'Question: {self.question}; Answer: {self.text} - {self.correct_answer}'
