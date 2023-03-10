# Generated by Django 4.1.7 on 2023-02-14 09:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='название')),
                ('description', models.TextField(blank=True, max_length=4096, verbose_name='Описание')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='рейтинг')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='год выпуска')),
                ('budget', models.IntegerField(default=1000000, verbose_name='бюджет')),
                ('currency', models.CharField(choices=[('EUR', 'Euros'), ('USD', 'US Dollars'), ('RUR', 'Rubles')], default='USD', max_length=3, verbose_name='валюта')),
                ('slug', models.SlugField(default='', unique=True)),
            ],
        ),
    ]
