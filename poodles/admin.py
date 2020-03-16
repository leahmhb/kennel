from django.contrib import admin
from poodles.models import Person, Poodle

# Register your models here.

admin.site.register(Person)
admin.site.register(Poodle)

admin.site.empty_value_display = ''

class PersonAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'mi', 'kennel_name')


class PoodleAdmin(admin.ModelAdmin):
	list_display = ('name_registered', 'name_call', 'sex', 'color')