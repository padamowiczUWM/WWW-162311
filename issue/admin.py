from django.contrib import admin

from issue.models import Issue, Category, Person, Position

# Register your models here.
admin.site.register(Category)
admin.site.register(Issue)

from django.contrib import admin



@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	readonly_fields = ['date_created']
	list_display = ['name', 'surname', 'sex', 'position', 'view_position']
	list_filter = ('position', 'date_created')

	@admin.display(empty_value='Stanowisko (Brak)')
	def view_position(self, obj):
		return f'{obj.position.name} ({obj.position.id})'

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
	list_filter = ('name',)