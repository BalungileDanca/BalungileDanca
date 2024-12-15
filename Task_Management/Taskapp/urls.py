from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('tasks', views.create_task, name='create_task'),
    path('tasks/<int:id>', views.get_task, name='get_task'),
    path('tasks/<int:id>/update', views.update_task, name='update_task'),
    path('tasks/<int:id>/delete', views.delete_task, name='delete_task'),
    #These views will allow clients to authenticate and get the JWT tokens.
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
