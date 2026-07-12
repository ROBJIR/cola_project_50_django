from django.urls import path
from .views import *

urlpatterns = [
    path('', imdb, name='imdb'),
    path('genre', genre, name='genre'),
    path('person', person, name='person'),
    path('movie', movie, name='movie'),
]