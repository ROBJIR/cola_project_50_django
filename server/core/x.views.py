from django.http.response import HttpResponse
from django.shortcuts import render
from random import randint

# Create your views here.
def home1(request):
    return HttpResponse('<h1><color = "red">Hello, world.</color></h1>')

def home2(request):
    return render(request, 'home2.html')

def hello(request,string: str="***"):
    return HttpResponse(f'<div>Hello {string}</div>')


def random(request, min_num: int, max_num: int):
    r_num = randint(min_num,max_num)
    return HttpResponse(f'The user entered the values {min_num} and {max_num}. The following number was drawn: {r_num}')