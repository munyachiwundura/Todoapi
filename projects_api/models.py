from django.db import models

# Create your models here.


def get_upload_path(instance, filename):
    return f"media/projects/{instance}/{filename}"


def upload_path(instance, filename):
    return f"media/projects/{instance}/{filename}"


class Project(models.Model):
    title = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    review = models.CharField(max_length=500)
    rating = models.IntegerField(default=5)
    reviewer = models.CharField(max_length=255)
    reviewer_image = models.ImageField(upload_to=get_upload_path)
    cover_image = models.ImageField(upload_to=get_upload_path)
    featured = models.BooleanField(default=False)
    link = models.URLField(max_length=2000)

    def __str__(self):
        return self.title


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=255)
    original = models.ImageField(upload_to=get_upload_path)
    caption = models.CharField(max_length=255)
    display_order = models.IntegerField()

    def __str__(self):
        return self.project_title
