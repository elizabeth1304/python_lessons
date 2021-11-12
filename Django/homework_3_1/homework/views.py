from django.shortcuts import render, HttpResponse
from datetime import datetime


def greeting(request):
    return HttpResponse("<h1><i>Welcome to our page!!</i></h1>")


def intro(request):
    return HttpResponse("Here's the introduction section.")


def date_time(request):
    return HttpResponse("Current date and time: {}".format(datetime.now()))


def task(request):
    d = dict()
    for x in range(1, 16):
        d[x] = x ** 2

    return HttpResponse('Dictionary {}'.format(d))
