from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin

from .admin_function import show_photo
from places.models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ["show_photo"]
    fields = ('img', 'show_photo', 'number_img')
    show_photo = show_photo


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
      ImageInline
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('place', 'img', 'number_img', 'show_photo')
    readonly_fields = ["show_photo"]
    show_photo = show_photo
