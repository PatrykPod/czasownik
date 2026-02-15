from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TimeLog
from datetime import datetime


@api_view(['POST'])
def save_logs(request):
    data = request.data

    user_id = data.get("user_id")
    logs = data.get("logs", [])

    created = []

    for log in logs:
        obj = TimeLog.objects.create(
            user_id=user_id,
            project_id=log["project_id"],
            start=log["start"],
            end=log["end"],
            duration=log["duration"]
        )
        created.append(obj.id)

    return Response({
        "status": "ok",
        "created": created
    })

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})
