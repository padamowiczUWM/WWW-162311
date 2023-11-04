from django.apps import AppConfig

class IssueConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'issue'

	def ready(self):
		from issue.models import Department, Category
		from django.db import connection

		all_tables = connection.introspection.table_names()

		if 'category' in all_tables:
			Category.objects.get_or_create(
				id=1,
				defaults=dict(
					name="Awaria sprzętu"
				)
			)
			Category.objects.get_or_create(
				id=2,
				defaults=dict(
					name="Błąd oprogramowania"
				)
			)

		if 'department' in all_tables:
			Department.objects.get_or_create(
				id=1,
				defaults=dict(
					name="IT"
				)
			)
			Department.objects.get_or_create(
				id=2,
				defaults=dict(

					name="HR"
				)
			)
