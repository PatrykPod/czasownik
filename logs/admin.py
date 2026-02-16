from django.contrib import admin
from .models import TimeLog
from django.db.models import Sum


def format_duration(seconds):
    seconds = int(seconds or 0)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h}:{m:02}:{s:02}"


@admin.register(TimeLog)
class TimeLogAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'project_id', 'start', 'end', 'duration_human')
    list_filter = ('user_id', 'project_id')
    search_fields = ('user_id', 'project_id')
    ordering = ('-start',)

    def duration_human(self, obj):
        return format_duration(obj.duration)
    duration_human.short_description = "Czas"

    # 🔥 RAPORT NA GÓRZE
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)

        try:
            queryset = response.context_data['cl'].queryset

            total = queryset.aggregate(total=Sum('duration'))['total'] or 0

            by_project = queryset.values('project_id').annotate(
                total=Sum('duration')
            ).order_by('-total')

            by_user = queryset.values('user_id').annotate(
                total=Sum('duration')
            ).order_by('-total')

            response.context_data['summary'] = {
                'total': format_duration(total),
                'by_project': [
                    (row['project_id'], format_duration(row['total']))
                    for row in by_project
                ],
                'by_user': [
                    (row['user_id'], format_duration(row['total']))
                    for row in by_user
                ]
            }

        except Exception:
            pass

        return response


    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)

        try:
            queryset = response.context_data['cl'].queryset
            total = queryset.aggregate(total=Sum('duration'))['total'] or 0

            self.message_user(
                request,
                f"Suma czasu: {format_duration(total)}"
            )

        except Exception:
            pass

        return response
