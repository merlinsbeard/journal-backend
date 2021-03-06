# Generated by Django 2.2.7 on 2019-11-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_auto_20181124_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='tag')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='page',
        ),
        migrations.AddField(
            model_name='page',
            name='tags',
            field=models.ManyToManyField(to='notebook.Tag'),
        ),
    ]
