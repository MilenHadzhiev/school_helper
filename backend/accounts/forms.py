from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from accounts.models import Student, User


class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    school = forms.CharField(max_length=100)
    grade_choices = (
        ('8', 'Осми клас'),
        ('9', 'Девети клас'),
        ('10', 'Десети клас'),
        ('11', 'Единадесети клас'),
        ('12', 'Дванадесети клас'),
    )

    grade = forms.ChoiceField(choices=grade_choices)

    # date_of_birth = forms.DateField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email is already taken')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.grade = self.cleaned_data['grade']
        # student.date_of_birth = self.cleaned_data['date_of_birth']
        student.save()
        return user


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    school = forms.CharField(max_length=100)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email is already taken')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.is_teacher = True
        user.is_staff = True

        if commit:
            user.save()
        return user


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].required = False
        self.fields['school'].required = False

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'school', 'profile_picture')
