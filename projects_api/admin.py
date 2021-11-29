from django.contrib import admin

from projects_api.models import Image, Project

# Register your models here.

admin.site.register(Project)
admin.site.register(Image)
