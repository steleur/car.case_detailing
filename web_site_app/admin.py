from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'picture', 'description')


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'type', 'price')


class CarImagesAdmin(admin.StackedInline):
    model = CarImages


class CarWorkAdmin(admin.StackedInline):
    model = CarWork


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('car', 'car_picture', 'works', 'slug',)
    inlines = [CarWorkAdmin, CarImagesAdmin]
    prepopulated_fields = {'slug': ('car',)}
