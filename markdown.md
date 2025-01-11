1. use Django Rest Framework's permission classes to enforce authentication.
2. add the IsAuthenticated permission class: Create_task view:
class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes= ([IsAuthenticated]) #  view can only be accessed by authenticated users
endpoint: 'api/Task_API/tasks/create/'
3. Retrieve a task using the task's ID, ensuring the user is authenticated:
serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
endpoint: 'api/Task_API/tasks/<int:pk>/'
4. Allow authenticated users to delete a task:
class TaskDeleteView(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
endpoint: 'api/Task_API/tasks/<int:pk>/delete/'
5. Allow authenticated users to update task details:
class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
endpoint: 'api/Task_API/tasks/<int:pk>/update/'


# Configure Authentication and permission in settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


# Test

Make a POST request to /api/user_management/users/login with the user's username and password the token is generated:

Request URL: http://127.0.0.1:8000/api/user_management/users/login

Method: POST

Headers:

Content-Type: application/json
Body:
{
    "username": "your_username",
    "password": "your_password"
}
Response:
{
    "token": "your_token"
}

# secure your API endpoints by:

Adding Authorization headers in API requests:

Authorization: Token <your_token>

