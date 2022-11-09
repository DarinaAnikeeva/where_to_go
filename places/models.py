from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
  title = models.CharField(
        verbose_name="Название места",
        max_length=200
  )

  description_short = models.TextField(
        verbose_name="Короткое описание",
        blank=False
  )

  description_long = HTMLField(
        verbose_name="Длинное описание",
        blank=True
  )

  lng = models.FloatField(
        verbose_name="Широта",
        null=False
  )

  lat = models.FloatField(
        verbose_name="Долгота",
        null=False
  )

  class Meta:
    ordering = ['id']

  def __str__(self):
    return self.title



class Image(models.Model):
  place = models.ForeignKey(
        Place,
        verbose_name="Название места",
        on_delete=models.CASCADE,
        related_name="images",
        blank=True,
        null=True
  )

  img = models.ImageField(
        verbose_name="Изображение",
        blank=False
  )

  number_img = models.IntegerField(
        verbose_name="Номер изображения",
        default=1,
        blank=True
  )

  class Meta:
    ordering = ['number_img']

  def __str__(self):
    return f'{self.number_img} {self.place}'
