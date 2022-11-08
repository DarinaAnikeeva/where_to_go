import json
import os
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from places.models import Place

def get_object(id):
    place = get_object_or_404(Place, pk=id)
    return place.title

def places(requests, place):
    place_info = {
        "title": place.title,
        "imgs": [image.img.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
              "lng": place.lng,
              "lat": place.lat
        }
    }
    file_path = os.path.join('static', 'places', f'{place.id}.json')
    with open(file_path, 'w', encoding='utf8') as json_file:
        json.dump(place_info, json_file, ensure_ascii=False)
    return file_path


def place_info(place):
    return {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": places(place)
          }
    }

def index(requests):
    places = Place.objects.all()
    context = {
      "places_info": {
          "type": "FeatureCollection",
          "features": [place_info(place) for place in places]
        }
    }
    return render(requests, 'index.html', context)
