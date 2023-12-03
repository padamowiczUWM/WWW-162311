from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, viewsets
from rest_framework.authentication import TokenAuthentication

from issue.models import Department
from issue.serializers import DepartmentSerializer
from user.permissions import IsSuperUser


class DepartmentViewSet(
	viewsets.GenericViewSet,
	mixins.RetrieveModelMixin,
	mixins.ListModelMixin,
	mixins.UpdateModelMixin,
	mixins.CreateModelMixin,
	mixins.DestroyModelMixin
):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (
		permissions.IsAuthenticated, IsSuperUser
	)

	serializer_class = DepartmentSerializer

	queryset = Department.objects.all()

	def get_permissions(self):
		if self.action in ['list', 'retrieve']:
			return [permissions.IsAuthenticated(),]

		return super().get_permissions()

	@swagger_auto_schema(
		operation_summary='Pojedynczy dział',
		tags=['Działy'],
		manual_parameters=[]
	)
	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Lista działów',
		tags=['Działy'],
		manual_parameters=[]
	)
	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Aktualizacja działu',
		tags=['Działy'],
		manual_parameters=[]
	)
	def update(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Utworzenie działu',
		tags=['Działy'],
		manual_parameters=[]
	)
	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Częściowa aktualizacja działu',
		tags=['Działy'],
		manual_parameters=[]
	)
	def partial_update(self, request, *args, **kwargs):
		return super().partial_update(request, *args, **kwargs)


	@swagger_auto_schema(
		operation_summary='Usuwanie działu',
		tags=['Działy'],
		manual_parameters=[]
	)
	def destroy(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)