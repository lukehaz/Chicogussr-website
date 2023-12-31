# Generated by Django 4.1.4 on 2023-04-22 01:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_leaderboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='login_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
