# Generated by Django 3.0.6 on 2020-05-31 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodwagon_backend', '0021_auto_20200531_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitemtruck',
            name='date_added',
        ),
    ]
