import json
import os
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from places.models import Place

def get_object(id):
    place = get_object_or_404(Place, pk=id)
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
    response = JsonResponse(place_info,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False,
                                               'indent': 2})
    return response


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
            "detailsUrl": reverse('place_info')
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
