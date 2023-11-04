from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, viewsets
from rest_framework.authentication import BasicAuthentication

from issue.models import Issue
from issue.serializers import IssueSerializer


class IssueViewSet(
	viewsets.GenericViewSet,
	mixins.RetrieveModelMixin,
	mixins.ListModelMixin,
	mixins.UpdateModelMixin,
	mixins.CreateModelMixin
):
	authentication_classes = (BasicAuthentication,)
	permission_classes = (
		permissions.IsAuthenticated,
	)

	serializer_class = IssueSerializer

	queryset = Issue.objects.all()

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
		manual_parameters=[]
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