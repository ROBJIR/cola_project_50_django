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

rows = Genre.objects.all().order_by('pk')
for row in rows:
    print(row.name)