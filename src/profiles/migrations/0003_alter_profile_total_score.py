# Generated by Django 3.2.4 on 2021-06-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_cities_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='total_score',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
