from django.contrib import admin
from todoapi.models import TodoItem, TodoCategory

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(TodoCategory)
