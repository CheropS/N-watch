# Generated by Django 3.2.8 on 2021-11-01 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0002_neighbourhood_occupants_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('user_id', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('neighbourhood_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.neighbourhood')),
            ],
        ),
    ]
