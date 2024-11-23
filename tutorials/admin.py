from django.contrib import admin
from .models import Unit

class UnitAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

admin.site.register(Unit, UnitAdmin)
