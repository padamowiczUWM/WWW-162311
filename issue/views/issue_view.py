from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from issue.models import Issue, IssueLog
from issue.serializers import IssueSerializer, IssueLogSerializer


class IssueViewSet(
	viewsets.GenericViewSet,
	mixins.RetrieveModelMixin,
	mixins.ListModelMixin,
	mixins.UpdateModelMixin,
	mixins.CreateModelMixin,
	mixins.DestroyModelMixin
):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (
		permissions.IsAuthenticated,
	)

	serializer_class = IssueSerializer

	queryset = Issue.objects.all()

	def filter_queryset(self, queryset):
		queryset = super().filter_queryset(queryset)

		department = self.request.GET.get('department')
		if department:
			queryset = queryset.filter(department_id=department)

		return queryset

	def perform_create(self, serializer):
		issue = serializer.save(creator=self.request.user)
		IssueLog.objects.create(
			name='Utworzenie zgłoszenia',
			user=self.request.user,
			issue=issue
		)

	def perform_update(self, serializer):
		issue = serializer.save(creator=self.request.user)
		IssueLog.objects.create(
			name='Aktualizacja zgłoszenia',
			user=self.request.user,
			issue=issue
		)

	@swagger_auto_schema(
		operation_summary='Pojedyncze zgłoszenie',
		tags=['Zgłoszenia'],
		manual_parameters=[]
	)
	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Lista zgłoszeń',
		tags=['Zgłoszenia'],
		manual_parameters=[
			openapi.Parameter(
				'department', openapi.IN_QUERY,
				description="ID działu",
				type=openapi.TYPE_NUMBER
			)
		]
	)
	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Aktualizacja zgłoszenia',
		tags=['Zgłoszenia'],
		manual_parameters=[]
	)
	def update(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Utworzenie zgłoszenia',
		tags=['Zgłoszenia'],
		manual_parameters=[]
	)
	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Częściowa aktualizacja zgłoszenia',
		tags=['Zgłoszenia'],
		manual_parameters=[]
	)
	def partial_update(self, request, *args, **kwargs):
		return super().partial_update(request, *args, **kwargs)


	@swagger_auto_schema(
		operation_summary='Usuwanie zgłoszenia',
		tags=['Zgłoszenia'],
		manual_parameters=[]
	)
	def destroy(self, request, *args, **kwargs):
		issue = self.get_object()

		if request.user != issue.creator:
			raise PermissionDenied('Nie posiadasz uprawnień do tego zgłoszenia.')

		return super().destroy(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Ilość stworzonych zgłoszeń w systemie',
		tags=['Zgłoszenia'],
		manual_parameters=[]
	)
	def get_issue_count(self, request):
		return Response(
			dict(
				all_count=Issue.objects.count(),
				user_count=Issue.objects.filter(creator=self.request.user).count()
			)
		)

	@swagger_auto_schema(
		operation_summary='Przypisanie zalogowanego użytkownika do zgłoszenia',
		tags=['Zgłoszenia'],
		manual_parameters=[]
	)
	def assign_to_me(self, request, pk):
		try:
			issue = Issue.objects.get(pk=pk)
		except Issue.DoesNotExist:
			raise Http404

		issue.performer = request.user
		issue.save()

		IssueLog.objects.create(
			name='Przypisanie sobie zgłoszenia.',
			user=self.request.user,
			issue=issue
		)

		return Response(status=status.HTTP_200_OK)

class IssueLogViewSet(
	viewsets.GenericViewSet,
	mixins.ListModelMixin,
):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (
		permissions.IsAuthenticated,
	)

	serializer_class = IssueLogSerializer

	queryset = IssueLog.objects.all()

	def get_queryset(self):
		return super().get_queryset().filter(issue_id=self.kwargs.get('issue_pk'))

	@swagger_auto_schema(
		operation_summary='Logi zgłoszenia',
		tags=['Zgłoszenia'],
		manual_parameters=[]
	)
	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)