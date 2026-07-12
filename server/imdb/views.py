from django.shortcuts import render
from django.template.defaultfilters import length

from .models import Genre, Person, Movie

# Create your views here.

def imdb(request):
    return render(request, 'rjdesign.html',{"web_name":"robertjiranek.eu","page_name":"imdb","page_body":"" })

def genre(request):
    genres = Genre.objects.all().order_by('name')
    countofrows = length(genres)
    html_body = ""
    for genre in genres:
        countofmovies = length(Genre.objects.get(id=id))
        html_body += f"<tr><td><small><i>{genre.pk}</i></small></td><td> {genre.name}</td><td>{countofmovies}</td></tr>\n"
    html_body = f"<table>\n<tr><th>id</th><th>name</th><th>count movies</th></tr>\n{html_body}\n</table>\n"
    html_body = f"<div>rows: {countofrows}</div>\n"

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