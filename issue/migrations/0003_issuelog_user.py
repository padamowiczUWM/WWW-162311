# Generated by Django 4.1.12 on 2023-12-03 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issue', '0002_issue_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuelog',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
