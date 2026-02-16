from django.http import FileResponse
import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


def frontend(request):
    file_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    return FileResponse(open(file_path, 'rb'))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('logs.urls')),
    path('', frontend),
]
