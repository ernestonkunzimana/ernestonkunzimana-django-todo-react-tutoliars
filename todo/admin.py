from functools import total_ordering
from django.contrib import admin

# Register your models here.

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Registering my Models are going to be done here

admin.site.register(Todo, TodoAdmin)
