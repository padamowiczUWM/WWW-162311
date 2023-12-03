from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, viewsets
from rest_framework.authentication import TokenAuthentication

from issue.models import Category
from issue.serializers import CategorySerializer
from user.permissions import IsSuperUser


class CategoryViewSet(
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

	serializer_class = CategorySerializer

	queryset = Category.objects.all()

	def get_permissions(self):
		if self.action in ['list', 'retrieve']:
			return [permissions.IsAuthenticated(),]

		return super().get_permissions()

	def filter_queryset(self, queryset):
		queryset = super().filter_queryset(queryset)

		department = self.request.GET.get('department')
		if department:
			queryset = queryset.filter(department_id=department)

		return queryset

	@swagger_auto_schema(
		operation_summary='Pojedyncza kategoria',
		tags=['Kategorie zgłoszeń'],
		manual_parameters=[]
	)
	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Lista kategorii',
		tags=['Kategorie zgłoszeń'],
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
		operation_summary='Aktualizacja kategorii',
		tags=['Kategorie zgłoszeń'],
		manual_parameters=[]
	)
	def update(self, request, *args, **kwargs):
		return super().update(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Utworzenie kategorii',
		tags=['Kategorie zgłoszeń'],
		manual_parameters=[]
	)
	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Częściowa aktualizacja kategorii',
		tags=['Kategorie zgłoszeń'],
		manual_parameters=[]
	)
	def partial_update(self, request, *args, **kwargs):
		return super().partial_update(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Usuwanie kategorii',
		tags=['Kategorie zgłoszeń'],
		manual_parameters=[]
	)
	def destroy(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)