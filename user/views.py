from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import GenericViewSet

from user.models import User
from user.permissions import IsSuperUser
from user.serializers import UserSerializer


class UserViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (
		permissions.IsAuthenticated, IsSuperUser
	)
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def get_permissions(self):
		if self.action in ['retrieve']:
			return [permissions.IsAuthenticated(),]

		return super().get_permissions()

	@swagger_auto_schema(
		operation_summary='Utworzenie użytkownika',
		tags=['Użytkownicy'],
		manual_parameters=[]
	)
	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Pojedynczy użytkownik',
		tags=['Użytkownicy'],
		manual_parameters=[]
	)
	def retrieve(self, request, *args, **kwargs):
		if request.user != self.get_object():
			raise PermissionDenied('Nie posiadasz uprawnień do tego konta.')

		return super().retrieve(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Lista użytkowników',
		tags=['Użytkownicy'],
		manual_parameters=[]
	)
	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

	@swagger_auto_schema(
		operation_summary='Usuwanie konta użytkownika',
		tags=['Użytkownicy'],
		manual_parameters=[]
	)
	def destroy(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)