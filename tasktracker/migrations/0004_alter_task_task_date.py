# Generated by Django 4.2 on 2023-04-14 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktracker', '0003_account_task_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateField(),
        ),
    ]
