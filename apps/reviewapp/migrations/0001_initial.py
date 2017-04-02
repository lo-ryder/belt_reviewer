# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookapp', '0001_initial'),
        ('logregapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_reviewed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_for_book', to='bookapp.Book')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_written', to='logregapp.User')),
            ],
        ),
    ]