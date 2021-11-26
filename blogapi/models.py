from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    cover = models.ImageField()
    text = tinymce_models.HTMLField()

    def __str__(self):
        return self.title
