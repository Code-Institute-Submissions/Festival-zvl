# Generated by Django 3.1 on 2020-08-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0009_auto_20200829_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='concert_time',
            field=models.CharField(default='20.00 uur', max_length=16),
        ),
    ]
