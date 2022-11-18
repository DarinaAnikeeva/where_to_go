from django.utils.html import format_html


def show_photo(self, obj):
    return format_html('<img src="{url}" style="max-height: 200px;">',
                       url=obj.img.url)
