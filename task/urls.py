from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, LoginUserView, RegisterUserView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('user/login/', LoginUserView.as_view(), name='login_user'),
    path('user/register/', RegisterUserView.as_view(), name='user_register'),
]