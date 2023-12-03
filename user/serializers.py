from rest_framework import serializers

from issue.serializers import DepartmentSerializer
from user.models import User


class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	department_data = DepartmentSerializer(source='department', read_only=True)

	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'department', 'department_data')

	def create(self, validated_data):
		user = User(
			username=validated_data['username'],
			email=validated_data['email'],
			department=validated_data['department'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name'],
		)
		user.set_password(validated_data['password'])
		user.save()
		return user