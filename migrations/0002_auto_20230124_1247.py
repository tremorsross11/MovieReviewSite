# Generated by Django 2.2.5 on 2023-01-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviePicker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviepickermodel',
            name='time',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]