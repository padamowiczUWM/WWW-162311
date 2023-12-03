from rest_framework import serializers

from issue.models import Category, Department, Issue, IssueLog


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'
		read_only_fields = ('updated_at', 'created_at')

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = '__all__'
		read_only_fields = ('updated_at', 'created_at')

class IssueSerializer(serializers.ModelSerializer):
	category_data = CategorySerializer(source='category', read_only=True)
	department_data = DepartmentSerializer(source='department', read_only=True)

	class Meta:
		model = Issue
		fields = '__all__'
		read_only_fields = ('updated_at', 'created_at', 'category_data', 'department_data', 'creator')

class IssueLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = IssueLog
		fields = '__all__'
		read_only_fields = ('updated_at', 'created_at')