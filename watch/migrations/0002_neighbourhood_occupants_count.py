# Generated by Django 3.2.8 on 2021-11-01 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='occupants_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]