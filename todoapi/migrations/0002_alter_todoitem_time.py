# Generated by Django 3.2.9 on 2021-12-05 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='time',
            field=models.DateField(),
        ),
    ]
