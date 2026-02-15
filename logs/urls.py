from django.urls import path
from .views import save_logs, health

urlpatterns = [
    path('logs/', save_logs),
    path('health/', health),
]
