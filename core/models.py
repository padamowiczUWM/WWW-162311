import datetime

from django.db import models


class Timestamp(models.Model):
	updated_at = models.DateTimeField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if self.pk:
			self.updated_at = datetime.datetime.now()
		return super().save(*args, **kwargs)
	class Meta:
		abstract = True


class DictionaryBase(Timestamp):
	name = models.CharField(max_length=128)

	class Meta:
		abstract = True