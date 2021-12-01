# Generated by Django 3.2.9 on 2021-11-30 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('project_summary', models.CharField(max_length=1255)),
            ],
        ),
    ]
