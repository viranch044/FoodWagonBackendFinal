# Generated by Django 3.0.6 on 2020-06-11 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodwagon_backend', '0029_auto_20200611_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemchef',
            name='end',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orderitemchef',
            name='start',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orderitemvenue',
            name='end',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orderitemvenue',
            name='start',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
