from django.contrib import admin
from .models import Person, Kennel

admin.site.empty_value_display = ''

admin.site.register(Person)
admin.site.register(Kennel)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mi')
