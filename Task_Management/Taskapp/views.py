from django.shortcuts import render
#POST /api/tasks: Create a new task
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Task

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    data = request.data

    # Validate that 'title' exists and is not empty
    if not data.get('title'):
        return Response({"error": "The 'title' field is required and cannot be null."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        task = Task.objects.create(
            title=data.get('title'),
            description=data.get('description', ''),
            priority=data.get('priority', 'medium'),
            due_date=data.get('due_date'),
            status='incomplete'
        )
        return Response({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "due_date": task.due_date,
            "status": task.status,
            "message": "Task created successfully."
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#GET /api/tasks/{id}: Retrieve a specific task

from django.shortcuts import get_object_or_404

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task(request, id):
    task = get_object_or_404(Task, pk=id)
    return Response({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "due_date": task.due_date,
        "status": task.status,
    }, status=status.HTTP_200_OK)

#PUT /api/tasks/{id}: Update an existing task
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, id):
    task = get_object_or_404(Task, pk=id)
    data = request.data
    try:
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.priority = data.get('priority', task.priority)
        task.due_date = data.get('due_date', task.due_date)
        task.status = data.get('status', task.status)
        task.save()
        return Response({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "due_date": task.due_date,
            "status": task.status,
            "message": "Task updated successfully."
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#DELETE /api/tasks/{id}: Delete a specific task

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return Response({"message": "Task deleted successfully."}, status=status.HTTP_200_OK)



