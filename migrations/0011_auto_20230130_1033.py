# Generated by Django 2.2.5 on 2023-01-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviePicker', '0010_auto_20230130_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviepickermodel',
            name='Rate',
            field=models.CharField(choices=[('4/10', '4/10'), ('3/10', '3/10'), ('6/10', '6/10'), ('1/10', '1/10'), ('0/10', '0/10'), ('7/10', '7/10'), ('9/10', '9/10'), ('5/10', '5/10'), ('10/10', '10/10'), ('8/10', '8/10'), ('2/10', '2/10')], default='0/10', max_length=10),
        ),
    ]
