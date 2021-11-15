from django.urls import path
from films import views

urlpatterns = [
    path('', views.home),
    path('rate', views.rate_fun),
    path('new_films', views.new_film),
    path('deleted', views.delete_film),
]