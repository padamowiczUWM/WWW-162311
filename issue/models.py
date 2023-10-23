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
	date_created = models.DateField(auto_now_add=True)

	def __str__(self):
		return f'{self.name} {self.surname}'

	class Meta:
		ordering = ['surname']