from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from films.models import Film


# Create your views here.


def home(request):
    films_list = Film.objects.all()
    return HttpResponse('Hello there!! {}'.format(films_list))


def rate_fun(request):
    rate = Film.objects.filter(film_rate=5)
    return HttpResponse('Here is some films with rate 5: {}, {}, {}.'.format(*rate))


def new_film(request):
    film = Film.objects.create(film_name='The Godfather', film_rate=3, is_published=True, status=0)
    return HttpResponse('New Film was added: "{}"'.format(film))


def delete_film(request):
    film = Film.objects.get(film_name="The Godfather")
    film.delete()
    return HttpResponse('This Film was deleted: "{}"'.format(film))
