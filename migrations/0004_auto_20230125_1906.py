# Generated by Django 2.2.5 on 2023-01-26 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MoviePicker', '0003_auto_20230124_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviepickermodel',
            old_name='genre',
            new_name='title',
        ),
    ]
