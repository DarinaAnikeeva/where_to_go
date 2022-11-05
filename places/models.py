from django.db import models

class Place(models.Model):
  title = models.CharField(max_length=200)
  imgs = models.TextField(blank=True)
  description_short = models.TextField(blank=False)
  description_long = models.TextField(blank=True)
  lng = models.FloatField(null=False)
  lat = models.FloatField(null=False)

  def __str__(self):
    return self.title
# Create your models here.
