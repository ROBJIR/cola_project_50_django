from django.shortcuts import render
from django.template.defaultfilters import length

from .models import Genre, Person, Movie

# Create your views here.

def imdb(request):
    html_body = ''
    html_body = f'{html_body}<a href="movie">movies</a> | \n'
    html_body = f'{html_body}<a href="person">persons</a> | \n'
    html_body = f'{html_body}<a href="genre">genres</a>\n'
    html_body = f'<div>{html_body}</div>\n'

    return render(request, 'rjdesign.html',{"web_name":"robertjiranek.eu","page_name":"imdb","page_body":html_body })

def genre(request):
    genres = Genre.objects.all().order_by('name')
    countrows = length(genres)
    html_body = ""
    for genre in genres:
        countmovies = length(Genre.objects.get(id=genre.pk))
        html_body += f"<tr><td><small><i>{genre.pk}</i></small></td><td> {genre.name}</td><td>{countmovies}</td></tr>\n"
    html_body = f"<table>\n<tr><th>id</th><th>name</th><th>count movies</th></tr>\n{html_body}\n</table>\n"
    html_body = f"{html_body}\n<div><small>rows: {countrows}</small></div>\n"

    return render(request, 'rjdesign.html',{"web_name":"robertjiranek.eu","page_name":"genres","page_body":html_body})

def person(request):
    persons = Person.objects.all().order_by('last_name','first_name')
    html_body = ""
    for person in persons:
        html_body += f"<tr><td><small><i>{person.pk}</i></small></td><td>{person.last_name}, {person.first_name}</td></tr>\n"
    html_body = f"<table>\n<tr><th>id</th><th>name</th></tr>\n{html_body}\n</table>\n"

    return render(request, 'rjdesign.html',{"web_name":"robertjiranek.eu","page_name":"persons","page_body":html_body})

def movie(request):
    movies = Movie.objects.all().order_by('title')
    html_body = ""
    for movie in movies:
        html_body += f"<tr><td><small><i>{movie.pk}</i></small></td><td> {movie.title}</td><td>{str(movie.year)}</td></tr>\n"
    html_body = f"<table>\n<tr><th>id</th><th>title</th><th>year</th></tr>\n{html_body}\n</table>\n"

    return render(request, 'rjdesign.html',{"web_name":"robertjiranek.eu","page_name":"movies","page_body":html_body})