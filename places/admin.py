from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.utils.html import format_html
from places.models import *


class ImageInline(SortableTabularInline):
  model = Image
  readonly_fields = ["preview"]
  fields = ('img', 'preview', 'number_img')

  def preview(self, obj):
      return format_html(f'<img src="{obj.img.url}" style="max-height: 100px;">')


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
      ImageInline
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
  fields = ('place', 'img', 'number_img', 'preview')
  readonly_fields = ["preview"]

  def preview(self, obj):
      return format_html(f'<img src="{obj.img.url}" style="max-height: 100px;">')
# Register your models here.
