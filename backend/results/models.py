from django.db import models

# Create your models here.
from accounts.models import User
from exams.models import Exam


class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f'{self.user.username} - {self.exam.name} - {self.score}%'
