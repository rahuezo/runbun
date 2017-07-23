# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    context = {}

    return render(request, 'runbun/index.html', context)


def gallery(request):
    context = {}

    return render(request, 'runbun/gallery.html', context)


def reviews(request):
    context = {}

    return render(request, 'runbun/reviews.html', context)


def contact(request):
    context = {}

    return render(request, 'runbun/contact.html', context)


def about(request):
    context = {}

    return render(request, 'runbun/about.html', context)


def signin(request):
    context = {}

    return render(request, 'runbun/signin.html', context)



def cart(request):
    context = {}

    return render(request, 'runbun/cart.html', context)
