from django.urls import path
from rest_framework import routers

from issue import lab_views
from issue.views import IssueViewSet

issue_router = routers.DefaultRouter()
issue_router.register('issue', IssueViewSet, basename='issue')

urlpatterns = [
    path('persons/', lab_views.person_list),
    path('persons/<int:pk>/', lab_views.person_detail),
    path('persons/update/<int:pk>/', lab_views.person_update),
    path('persons/delete/<int:pk>/', lab_views.person_delete),
    path('teams/', lab_views.team_list),
    path('teams/<int:pk>/', lab_views.team_detail),
    path('teams/<int:pk>/members/', lab_views.team_members),
]

urlpatterns += issue_router.urls