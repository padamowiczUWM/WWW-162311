from django.urls import path
from rest_framework import routers

from issue import lab_views
from issue.views import IssueViewSet

issue_router = routers.DefaultRouter()
issue_router.register('issue', IssueViewSet, basename='issue')

urlpatterns = [
    path('persons/', lab_views.PersonList.as_view()),
    path('persons/<int:pk>/', lab_views.PersonDetail.as_view()),
    path('teams/', lab_views.TeamList.as_view()),
    path('teams/<int:pk>/', lab_views.TeamDetail.as_view()),
]

urlpatterns += issue_router.urls