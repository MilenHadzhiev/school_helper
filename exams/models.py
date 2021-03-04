from random import shuffle

from django.db import models

# Create your models here.
from accounts.models import Subject, User


class Exam(models.Model):
    name = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    # time = models.IntegerField(help_text='Продължителност на теста')
    required_score_to_pass = models.IntegerField(help_text="Процент верни отговори за Среден (3)")
    required_score_four = models.IntegerField(help_text="Процент верни отговори за Добър (3.50)")
    required_score_five = models.IntegerField(help_text="Процент верни отговори за Много добър (4.50)")
    required_score_six = models.IntegerField(help_text="Процент верни отговори за Отличен (5.50)")

    def __str__(self):
        return f'{self.name}-{self.subject}'

    def get_questions(self):
        questions = list(self.question_set.all())
        shuffle(questions)
        return questions
