# Generated by Django 3.2 on 2022-04-18 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='board',
        ),
        migrations.AddField(
            model_name='playerboard',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
