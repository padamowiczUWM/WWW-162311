"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core import settings

schema_view = get_schema_view(
	openapi.Info(
		title="Issue API",
		default_version=f'0.0.1',
		contact=openapi.Contact(email="patrykadam.dev@gmail.com"),
		license=openapi.License(name="Beta"),
	),
	url=f'http://127.0.0.1:8000/',
	public=True,
	permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(r'swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'admin/', admin.site.urls),
	path(r'api/', include('issue.urls')),
	path(r'api/', include('user.urls')),
	path(r"__debug__/", include("debug_toolbar.urls")),
]
