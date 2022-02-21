from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from backend.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('lessons/', include('classes.urls')),
    path('notes/', include('notes.urls')),
    path('exams/', include('exams.urls', namespace='exams')),
    # path('api-auth/', include('rest_framework.urls')),
    path('school-app-administration/', admin.site.urls),
    # path('api/', include('classes.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
