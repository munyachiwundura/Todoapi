# Generated by Django 3.2.9 on 2021-12-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_api', '0009_auto_20211203_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='color',
            field=models.CharField(default='pink', max_length=255),
            preserve_default=False,
        ),
    ]
