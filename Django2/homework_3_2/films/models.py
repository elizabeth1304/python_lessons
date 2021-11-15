from django.db import models
from helpers.choices import STATUS_CHOICES


class Film(models.Model):
    film_name = models.CharField("The film's title", max_length=256)
    film_rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField()
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.film_name
