# Generated by Django 3.0.7 on 2020-06-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]