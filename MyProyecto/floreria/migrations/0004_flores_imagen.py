# Generated by Django 2.2.7 on 2019-12-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floreria', '0003_remove_flores_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='flores',
            name='imagen',
            field=models.ImageField(null=True, upload_to='flores'),
        ),
    ]
