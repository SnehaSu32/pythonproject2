# Generated by Django 4.1 on 2022-09-20 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_heros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heros',
            name='name',
            field=models.CharField(max_length=2500),
        ),
    ]
