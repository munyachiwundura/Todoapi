from django.db import models

# Create your models here.
class MailItem(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    company = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    project_summary = models.CharField(max_length=1255)

    def __str__(self):
        return self.name
