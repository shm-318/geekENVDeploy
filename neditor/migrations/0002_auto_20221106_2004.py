# Generated by Django 3.2.5 on 2022-11-06 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neditor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body_default',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_textfield',
        ),
    ]
