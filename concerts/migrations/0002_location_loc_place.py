# Generated by Django 3.1 on 2020-08-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='loc_place',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]