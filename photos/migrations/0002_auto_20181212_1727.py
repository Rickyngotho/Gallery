# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-12 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('pic_image', models.ImageField(upload_to='pics/')),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='pic',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Editor'),
        ),
        migrations.AddField(
            model_name='pic',
            name='tags',
            field=models.ManyToManyField(to='photos.tags'),
        ),
    ]
