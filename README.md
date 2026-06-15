# DEMO1
Repo de DEMO Init DJANGO


On commence par creer un environnement virtuel venv (pour garder les packages à disposition).
py -3.12 -m venv .venv

 
# Windows :
.venv\Scripts\activate

    >bash : source .venv/Scripts/activate

# macOS / Linux :
source .venv/bin/activate
 
pip install --upgrade pip
pip install Django
django-admin --version


## Creer un projet DJANGO : 
django-admin startproject premierprojet .

python manage.py runserver    === npm dev start 
# Visiter http://127.0.0.1:8000


