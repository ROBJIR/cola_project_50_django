from django.urls import path
from .views import *

urlpatterns = [
    path('', calculator, name='calculator'),
    path('<str:operator>/', calculator, name='calculator0'),
    path('<str:operator>/<int:num1>/', calculator, name='calculator1'),
    path('<str:operator>/<int:num1>/<int:num2>/', calculator, name='calculator2'),
]