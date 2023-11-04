from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ['department_id']

	department = models.ForeignKey(
		"issue.Department",
		on_delete=models.DO_NOTHING
	)

	class Meta:
		db_table = "user"
