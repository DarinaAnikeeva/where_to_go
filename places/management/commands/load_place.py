import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('url', help=u'Ссылка на json c данными точки')

    def download_images(self, place_info, place):
        images = place_info.get('imgs', [])
        for number, img_url in enumerate(images, start=1):
            response = requests.get(img_url)
            response.raise_for_status()
            image = ContentFile(
                response.content,
                name=f'{number}_{place_info["title"]}.jpg'
            )
            Image.objects.create(
                place=place,
                img=image,
                number_img=number
            )

        print('Точка создана!')

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        response = requests.get(url)
        response.raise_for_status()
        place_info = response.json()
        place, created = Place.objects.get_or_create(
            title=place_info['title'],
            lng=place_info["coordinates"]["lng"],
            lat=place_info["coordinates"]["lat"],
            defaults={
                'description_short': place_info.get("description_short", ''),
                'description_long': place_info.get("description_long", '')
                      },
            )
        if created:
            self.download_images(place_info, place)
