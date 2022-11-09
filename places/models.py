from django.db import models

class Place(models.Model):
  title = models.CharField(max_length=200)
  description_short = models.TextField(blank=False)
  description_long = models.TextField(blank=True)
  lng = models.FloatField(null=False)
  lat = models.FloatField(null=False)

  class Meta:
    ordering = ['id']

  def __str__(self):
    return self.title



class Image(models.Model):
  place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images", blank=True, null=True)
  img = models.ImageField(blank=False)
  number_img = models.IntegerField(default=1, blank=True)

  class Meta:
    ordering = ['number_img']

  def __str__(self):
    return f'{self.number_img} {self.place}'
