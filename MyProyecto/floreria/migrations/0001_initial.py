# Generated by Django 2.2.6 on 2019-11-07 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flores',
            fields=[
                ('name', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('valor', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pasw', models.CharField(max_length=12)),
            ],
        ),
    ]
