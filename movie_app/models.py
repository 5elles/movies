from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    ]
    first_name = models.CharField(max_length=100, blank=True, verbose_name= 'имя')
    last_name = models.CharField(max_length=100, blank=False, verbose_name= 'фамилия')
    gender = models.CharField(max_length=1, default=MALE, choices=GENDERS)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актёр {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('actor-detail', args=[self.id])


class Director(models.Model):
    first_name = models.CharField(max_length=100, blank=True, verbose_name= 'имя')
    patronymic = models.CharField(max_length=100, blank=True, verbose_name= 'отчество')
    last_name = models.CharField(max_length=100, blank=False, verbose_name= 'фамилия')
    director_email = models.EmailField(default='-', verbose_name='email')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('director-detail', args=[self.id])


class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUR = 'RUR'

    CURRENCY_CHOICES = [
        (EURO, 'Euros'),
        (USD, 'US Dollars'),
        (RUR, 'Rubles'),
    ]

    name = models.CharField(max_length=40, verbose_name='название')
    description = models.TextField(max_length=4096, blank=True, verbose_name='описание')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name='рейтинг'
    )
    year = models.IntegerField(null=True, blank=True, verbose_name='год выпуска')
    budget = models.IntegerField(default=1000000, verbose_name='бюджет')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD, verbose_name='валюта')
    slug = models.SlugField(null=False, db_index=True, unique=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, verbose_name='режиссёр')
    actors = models.ManyToManyField(Actor, verbose_name='актёры')

    def save(self, *args, **kwargs):  # заполнение поля slug
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - id:{self.id}, рейтинг: {self.rating}%'