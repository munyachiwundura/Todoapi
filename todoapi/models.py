from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save


# Create your models here.


def get_upload_path(instance, filename):
    return f"todos/category_images/{instance}/{filename}"


class TodoCategory(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=25)
    icon = models.ImageField(upload_to=get_upload_path)

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(TodoCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    time = models.DateTimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    status = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.title
