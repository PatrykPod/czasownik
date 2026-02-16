from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TimeLog
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def save_logs(request):
    data = request.data

    user_id = data.get("user_id")
    logs = data.get("logs", [])

    for log in logs:
        TimeLog.objects.create(
            user_id=user_id,
            project_id=log["project_id"],
            start=log["start"],
            end=log["end"],
            duration=log["duration"]
        )

    return Response({"status": "ok"})

@api_view(['GET'])
def health(request):
    return Response({
        "status": "ok",
        "app": "czasownik"
    })
