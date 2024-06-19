# Generated by Django 5.0.4 on 2024-06-19 10:55

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_list', app.models.ListField()),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='creation_year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]