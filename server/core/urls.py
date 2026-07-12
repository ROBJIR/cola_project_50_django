from django.urls import path, include
from .views import *

urlpatterns = [
    path ('', home, name = 'home'),
    path('sinfo/', sinfo, name='sinfo'),
    path('calculator/', include('calculator.urls')),
    path('imbd/', include('imdb.urls')),
]
