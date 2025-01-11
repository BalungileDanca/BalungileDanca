from django.urls import path
from .views import (
     UserRegisterView, login_user, logout_user, UserListView, UserDetailView, UserUpdateView, UserDeleteView, UsercreateView
)

urlpatterns = [
    # User authentication endpoints
    path('users/register/', UserRegisterView.as_view(), name='user-register'),
    path('users/login/', login_user, name='user-login'),
    path('users/logout/', logout_user, name='user-logout'),

    # User CRUD endpoints
   
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]