from django.db import models

class Timestamp(models.Model):
	updated_at = models.DateTimeField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

class DictionaryBase(Timestamp):
	name = models.CharField(max_length=128)

	class Meta:
		abstract = True