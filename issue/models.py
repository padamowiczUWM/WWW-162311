import datetime

from django.db import models

from core.models import DictionaryBase


class Issue(DictionaryBase):
	class Status:
		NEW = 0
		IN_PROGRESS = 1
		DONE = 2

		choices = (
			(NEW, "Nowe"),
			(IN_PROGRESS, "W trakcie"),
			(DONE, "Zakończone")
		)

	class Priority:
		LOW = 0
		MEDIUM = 1
		HIGH = 2

		choices = (
			(LOW, "Niski"),
			(MEDIUM, "Średni"),
			(HIGH, "Wysoki")
		)
	creator = models.ForeignKey(
		"user.User",
		on_delete=models.DO_NOTHING
	)
	performer = models.ForeignKey(
		"user.User",
		null=True,
		blank=True,
		related_name='performer',
		on_delete=models.DO_NOTHING
	)
	description = models.TextField(null=True, blank=True)
	category = models.ForeignKey(
		"issue.Category",
		on_delete=models.DO_NOTHING
	)
	priority = models.IntegerField(choices=Priority.choices)
	status = models.IntegerField(choices=Status.choices)
	department = models.ForeignKey(
		"issue.Department",
		on_delete=models.DO_NOTHING
	)

	class Meta:
		db_table = 'issue'


class IssueLog(DictionaryBase):
	user = models.ForeignKey(
		"user.User",
		on_delete=models.DO_NOTHING
	)

	issue = models.ForeignKey(
		"issue.Issue",
		on_delete=models.DO_NOTHING
	)

	class Meta:
		db_table = 'issue_log'
		ordering = ['-id']


class Category(DictionaryBase):
	department = models.ForeignKey(
		'issue.Department',
		on_delete=models.DO_NOTHING
	)

	class Meta:
		db_table = 'category'


class Department(DictionaryBase):
	class Meta:
		db_table = 'department'
