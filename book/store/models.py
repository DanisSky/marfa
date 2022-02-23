import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Album(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=False)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Service(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=False)
    price = models.FloatField(null=False)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Book(models.Model):
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.name} {self.year}'
