import os
import sys
from pathlib import Path

# nastaveni
# Složka obsahující manage.py
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

import django

django.setup()

from imdb.models import Genre
# ---
genress = Genre.objects.all().values_list().order_by('name')
print(genress)
for genre in genress:
    # print (genre)
    print(f"{genre[0]}: {genre[1]}")


genres = Genre.objects.all().filter(name__iregex=r"^[cH]").order_by('name')
for genre in genres:
    print(genre.name)
# ---

# GENRE - zanr filnu

g = Genre.objects.create(name='Action')
g = Genre.objects.create(name='Comedy')
g = Genre.objects.create(name='Drama')
g = Genre.objects.create(name='Horror')
g = Genre.objects.create(name='Sci-Fi')
g = Genre.objects.create(name='Fantasy')
g = Genre.objects.create(name='Romance')
g = Genre.objects.create(name='Thriller')
g = Genre.objects.create(name='Adventure')
g = Genre.objects.create(name='Documentary')

rows = Genre.objects.all().order_by('name')
for row in rows:
    print(row.name)

# Movies