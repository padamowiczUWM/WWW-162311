from django.urls import path
from rest_framework import routers

from issue import lab_views
from issue.views import IssueViewSet

issue_router = routers.DefaultRouter()
issue_router.register('issue', IssueViewSet, basename='issue')

urlpatterns = [
    path('persons/', lab_views.person_list),
    path('persons/<int:pk>/', lab_views.person_detail),
    path('teams/', lab_views.team_list),
    path('teams/<int:pk>/', lab_views.team_detail),
]

urlpatterns += issue_router.urls