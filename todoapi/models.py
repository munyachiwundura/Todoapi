from django.db import models

# Create your models here.

class TodoItem (models.Model):
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    status = models.BooleanField(default=False, null=False, blank=False)

