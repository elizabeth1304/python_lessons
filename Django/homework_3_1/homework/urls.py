from django.urls import path
from homework import views

urlpatterns = [
    path('', views.greeting, name='greeting'),
    path('intro/', views.intro, name='introduction'),
    path('time/', views.date_time, name='time'),
    path('task/', views.task, name='task'),
]