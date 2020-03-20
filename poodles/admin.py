from django.contrib import admin
from poodles.models import Poodle

# Register your models here.


admin.site.register(Poodle)

admin.site.empty_value_display = ''


class PoodleAdmin(admin.ModelAdmin):
    list_display = ('name_registered', 'name_call', 'sex', 'color')
