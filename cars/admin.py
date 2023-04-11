from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10px" />'.format(object.car_photo.url))
    thumbnail.short_description = 'Car Image'
    list_display = ('id', 'thumbnail', 'car_title', 'model', 'color', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'description', 'city', 'state', 'year', 'body_style', 'color')
    list_filter = ('city', 'model', 'year', 'body_style', 'fuel_type')
    list_per_page = 25

admin.site.register(Car, CarAdmin)