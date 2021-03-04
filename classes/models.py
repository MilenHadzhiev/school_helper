from django.db import models

from accounts.models import Subject, User
from cloudinary import models as cloudinary_models


class Lesson(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    # image = models.ImageField(
    #     upload_to='lesson_pics/',
    #     blank=True,
    #     default='',
    # )
    image = cloudinary_models.CloudinaryField('image')

    def __str__(self):
        return self.title

# class Exam(models.Model):
#     pass
