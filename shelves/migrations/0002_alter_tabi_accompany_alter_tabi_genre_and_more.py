# Generated by Django 4.0.6 on 2022-08-15 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelves', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabi',
            name='accompany',
            field=models.CharField(max_length=10, verbose_name='同行者'),
        ),
        migrations.AlterField(
            model_name='tabi',
            name='genre',
            field=models.CharField(max_length=40, verbose_name='ジャンル'),
        ),
        migrations.AlterField(
            model_name='tabi',
            name='place',
            field=models.CharField(max_length=20, verbose_name='場所'),
        ),
        migrations.AlterField(
            model_name='tabi',
            name='title',
            field=models.CharField(max_length=30, verbose_name='旅タイトル'),
        ),
    ]
