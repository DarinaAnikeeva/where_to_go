from django.contrib import admin
from places.models import *

class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
      ImageInline
    ]

admin.site.register(Image)
# Register your models here.
