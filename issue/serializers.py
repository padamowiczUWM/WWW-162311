from rest_framework import serializers
from issue.models import *

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
	category_data = CategorySerializer(source='category', read_only=True)
	department_data = DepartmentSerializer(source='department', read_only=True)

	class Meta:
		model = Issue
		fields = '__all__'


class PositionSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True)
	description = serializers.CharField(required=False)

	def create(self, validated_data):
		return Position.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.description = validated_data.get('description', instance.description)
		instance.save()
		return instance


class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = '__all__'
		read_only_fields = ['id']