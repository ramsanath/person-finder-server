# Generated by Django 2.2 on 2019-04-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchee',
            name='height_cm',
            field=models.IntegerField(null=True, verbose_name='height in cm'),
        ),
    ]
