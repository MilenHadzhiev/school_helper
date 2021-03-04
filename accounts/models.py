from django.contrib.auth.models import AbstractUser
from django.db import models

from cloudinary import models as cloudinary_models

class Subject(models.Model):
    another = 'друг'
    subjects_choices = [
        ('БЕЛ', 'Български език и литература'),
        ('Мат', 'Математика'),
        ('АЕ', 'Английски език'),
        ('НЕ', 'Немски език'),
        ('Ф', 'Физика'),
        ('Био', 'Биология'),
        ('Х', 'Химия'),
        ('Гео', 'География'),
        ('Ист', 'История'),
        ('ИТ', 'Информационни Технологии'),
        (another, another),
    ]
    title = models.CharField(choices=subjects_choices, max_length=30, default=another)

    def __str__(self):
        return self.title


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    school = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # date_of_birth = models.DateField(blank=True, default='0000-00-00')

    # profile_picture = models.ImageField(
    #     upload_to='profile_pics/',
    #     blank=True,
    #     default='',
    # )

    profile_picture = cloudinary_models.CloudinaryField('image')

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    grade_choices = [
        ('8', 'Осми клас'),
        ('9', 'Девети клас'),
        ('10', 'Десети клас'),
        ('11', 'Единадесети клас'),
        ('12', 'Дванадесети клас'),
    ]
    grade = models.CharField(
        max_length=2,
        choices=grade_choices,
    )

    def __str__(self):
        return self.user.username
