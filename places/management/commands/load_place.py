import requests
import os
from django.core.management.base import BaseCommand
from places.models import Place, Image

class Command(BaseCommand):
    def add_arguments(self, parser):
      parser.add_argument('url', help=u'Ссылка на json c данными точки')

    def handle(self, *args, **kwargs):
      url = kwargs['url']
      response = requests.get(url)
      response.raise_for_status()
      place_info = response.json()
      place = Place.objects.get_or_create(title=place_info['title'],
                                          description_short=place_info["description_short"],
                                          description_long=place_info["description_long"],
                                          lat=place_info["coordinates"]["lat"],
                                          lng=place_info["coordinates"]["lng"],
                                          )

      for number, img_url in enumerate(place_info["imgs"], start=1):
        response = requests.get(img_url)
        response.raise_for_status()
        image_name = f'{number}_{place_info["title"]}.jpg'
        file_path = os.path.join('media', image_name)
        with open(file_path, 'wb') as file:
          file.write(response.content)
        Image.objects.get_or_create(place=place[0], img=image_name, number_img=number)

      print('Точка создана!')


