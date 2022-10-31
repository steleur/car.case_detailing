from django.shortcuts import render, redirect
import json
from .models import *

import telebot

bot = telebot.TeleBot('')


def send_message(name, phone_number, service, text):
    result = f'*Имя:* {name}\n*Номер телефона:* {phone_number}\n*Интересующая услуга:* {service}\n*Сообщение:* {text}\n'
    bot.send_message('859964516', result, parse_mode='markdown')


# Create your views here.
def home(request):
    service = Services.objects.all()
    context = {'services': service,}
    return render(request, 'home.html', context)


def services(request):
    service = Services.objects.all()
    price = Price.objects.all()
    context = {'services': service, 'price': price}
    return render(request, 'services.html', context)


def gallery(request):
    gallery = Gallery.objects.all()
    context = {'gallery': gallery}
    return render(request, 'gallery.html', context)


def gallery_page(request, slug):
    gallery_car = Gallery.objects.get(slug=slug)
    images = CarImages.objects.all()
    car_work = CarWork.objects.all()
    context = {'gallery': gallery_car, 'image': images, 'car_work': car_work, }
    return render(request, 'car.html', context)


def certificates(request):
    return render(request, 'certificates.html')


def contacts(request):
    if request.method == 'POST':
        data = dict(request.POST)
        name, phone_number, service, text = data.get('name')[0], data.get('phone_number')[0], data.get('service')[0], \
                                            data.get('text')[0]
        send_message(name, phone_number, service, text)
        return redirect(request.META['HTTP_REFERER'])
    return render(request, 'contacts.html')
