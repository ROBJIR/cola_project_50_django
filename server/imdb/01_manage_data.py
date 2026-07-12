from imdb.models import Genre

for genre in Genre.objects.all():
    print(genre.name)