from django.urls import re_path, include
from rest_framework import routers
from issue.views import IssueViewSet, CategoryViewSet, DepartmentViewSet, IssueLogViewSet

drf_router = routers.DefaultRouter()
drf_router.register('issue', IssueViewSet, basename='issue')
drf_router.register('category', CategoryViewSet, basename='category')
drf_router.register('department', DepartmentViewSet, basename='department')

drf_router2 = routers.DefaultRouter()
drf_router2.register('log', IssueLogViewSet, basename='issue_log')

urlpatterns = [
	re_path(r'^issue/(?P<issue_pk>[0-9]+)/', include(drf_router2.urls)),
	re_path(r'^issue/count', IssueViewSet.as_view({
		'get': 'get_issue_count'
	})),
	re_path(r'^issue/(?P<pk>[0-9]+)/assign-to-me', IssueViewSet.as_view({
		'post': 'assign_to_me'
	})),
]

urlpatterns = drf_router.urls + urlpatterns