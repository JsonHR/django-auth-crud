# Generated by Django 3.2.16 on 2023-05-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='dataCompleted',
            new_name='dateCompleted',
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]