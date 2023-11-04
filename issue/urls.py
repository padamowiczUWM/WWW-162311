from rest_framework import routers
from issue.views import IssueViewSet

issue_router = routers.DefaultRouter()
issue_router.register('issue', IssueViewSet, basename='issue')

urlpatterns = issue_router.urls