# Generated by Django 3.2.8 on 2021-11-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0005_rename_business_name_business_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
