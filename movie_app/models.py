from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=100, blank=True, verbose_name= 'имя')
    patronymic = models.CharField(max_length=100, blank=True, verbose_name= 'отчество')
    last_name = models.CharField(max_length=100, blank=False, verbose_name= 'фамилия')
    director_email = models.EmailField(default='-', verbose_name='email')

    def __str__(self):
        return f'' \
               f'{self.last_name} ' \
               f'{self.first_name} ' \
               f'{self.patronymic} ' \
               f'| email: {self.director_email} | '



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

    def save(self, *args, **kwargs):  # заполнение поля slug
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - id:{self.id}, рейтинг: {self.rating}%'