# Generated by Django 2.2.5 on 2023-01-26 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MoviePicker', '0004_auto_20230125_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviepickermodel',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='moviepickermodel',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='moviepickermodel',
            old_name='review',
            new_name='Review',
        ),
        migrations.RenameField(
            model_name='moviepickermodel',
            old_name='title',
            new_name='Title',
        ),
    ]