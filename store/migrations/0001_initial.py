# Generated by Django 3.1.7 on 2021-03-20 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(verbose_name='Дата')),
                ('num_pages', models.IntegerField(verbose_name='Страницы')),
                ('genre', models.CharField(max_length=255, null=True)),
            ],
            options={
                'ordering': ['genre'],
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(verbose_name='Дата')),
                ('type', models.TextField(max_length=255, null=True)),
                ('publisher', models.TextField(max_length=255, null=True, verbose_name='Издатель')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
