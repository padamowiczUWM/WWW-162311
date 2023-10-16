from django.db import models

from core.models import DictionaryBase

class Issue(DictionaryBase):
	class Status(object):
		NEW = 0
		IN_PROGRESS = 1
		DONE = 2

		choices = (
			(NEW, "Nowe"),
			(IN_PROGRESS, "W trakcie"),
			(DONE, "Zakończone")
		)

	description = models.TextField(null=True, blank=True)
	category = models.ForeignKey(
		"issue.Category",
		on_delete=models.DO_NOTHING
	)
	status = models.IntegerField(choices=Status.choices)

	class Meta:
		db_table = 'issue'

class Category(DictionaryBase):
	class Meta:
		db_table = 'category'
