from django.contrib import admin

from accounts.models import Subject, Student, User

admin.site.register(Subject)
admin.site.register(User)
admin.site.register(Student)
