from django.db import models

class TimeLog(models.Model):
    user_id = models.CharField(max_length=50)
    project_id = models.CharField(max_length=100)

    start = models.DateTimeField()
    end = models.DateTimeField()

    duration = models.FloatField()  # sekundy

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.project_id}"
