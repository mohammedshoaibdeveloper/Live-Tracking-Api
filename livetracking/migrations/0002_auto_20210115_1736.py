# Generated by Django 3.1.5 on 2021-01-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livetracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='latitude',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='signup',
            name='longitude',
            field=models.CharField(default='', max_length=100),
        ),
    ]
