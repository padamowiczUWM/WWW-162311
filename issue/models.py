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
	issue = models.ForeignKey(
		"issue.Issue",
		on_delete=models.DO_NOTHING
	)

	class Meta:
		db_table = 'issue_log'


class Category(DictionaryBase):
	class Meta:
		db_table = 'category'


class Department(DictionaryBase):
	class Meta:
		db_table = 'department'


# region LAB
class Position(models.Model):
	name = models.CharField(max_length=128, blank=False)
	description = models.TextField(
		blank=True,
		null=True
	)


class Person(models.Model):
	class SexType(models.IntegerChoices):
		MAN = 1
		WOMAN = 2
		OTHER = 3

	name = models.CharField(max_length=64, blank=False)
	surname = models.CharField(max_length=64, blank=False)
	sex = models.IntegerField(choices=SexType.choices)
	position = models.ForeignKey(
		'Position',
		on_delete=models.DO_NOTHING
	)
	month_created = models.PositiveSmallIntegerField(default=datetime.datetime.now().strftime("%m"))
	date_created = models.DateField(auto_now_add=True)

	team = models.ForeignKey(
		"issue.Team",
		on_delete=models.DO_NOTHING
	)

	owner = models.ForeignKey(
		"user.User",
		on_delete=models.DO_NOTHING
	)


	def __str__(self):
		return f'{self.name} {self.surname}'

	class Meta:
		ordering = ['surname']
		permissions = [
			("can_view_other_persons", "Pozwala wyświetlać obiekty Person, których użytkownik nie jest właścicielem"),
		]


class Team(models.Model):
	name = models.CharField(max_length=60)
	country = models.CharField(max_length=2)

	def __str__(self):
		return f"{self.name}"

# endregion
