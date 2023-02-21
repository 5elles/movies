# Generated by Django 4.1.7 on 2023-02-21 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movie_app.director', verbose_name='режиссёр'),
        ),
        migrations.AlterField(
            model_name='director',
            name='director_email',
            field=models.EmailField(default='-', max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='director',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, max_length=4096, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]