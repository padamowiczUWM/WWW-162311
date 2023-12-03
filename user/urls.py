from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from user.views import UserViewSet

drf_router = routers.DefaultRouter()
drf_router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('auth/token/', obtain_auth_token),
]

urlpatterns += drf_router.urls