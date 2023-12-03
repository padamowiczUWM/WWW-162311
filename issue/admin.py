from django.contrib import admin

from issue.models import Issue, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Issue)
