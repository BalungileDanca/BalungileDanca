#  authentication setup
confuger the settings:
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
1. use Django Rest Framework's permission classes to enforce authentication.
2. add the IsAuthenticated permission class: Create_task view:
@api_view(['POST'])
@permission_classes([IsAuthenticated]) #  view can only be accessed by authenticated users
def create_task(request)
3. Retrieve a task using the task's ID, ensuring the user is authenticated:
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_task(request, id):
4. Allow authenticated users to delete a task:
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, id):
5. Allow authenticated users to update task details:
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, id):

# Configure JWT in settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Add Token Endpoints

/api/token/: For obtaining access and refresh tokens.
/api/token/refresh/: For refreshing the access token using the refresh token.

path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

# Test

Make a POST request to /api/token/ with the user's username and password:

Request URL: http://127.0.0.1:8000/api/token/

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
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}

# secure your API endpoints by:

Adding Authorization headers in API requests:

Authorization: Bearer <your_access_token>
