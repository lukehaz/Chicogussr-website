# Generated by Django 4.1.4 on 2023-04-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_score_average_score_score_lowest_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='average_score',
            field=models.FloatField(default=0.0),
        ),
    ]