# Generated by Django 3.2.4 on 2021-06-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_status_score', models.PositiveIntegerField(blank=True, null=True)),
                ('language_score', models.PositiveIntegerField(blank=True, null=True)),
                ('prof_exp_score', models.PositiveIntegerField(blank=True, null=True)),
                ('education_score', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
