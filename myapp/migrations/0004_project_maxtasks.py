# Generated by Django 4.1.7 on 2023-03-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_task_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='maxtasks',
            field=models.IntegerField(default=20),
        ),
    ]
