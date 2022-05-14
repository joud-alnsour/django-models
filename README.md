# Django Models
## Project: Snacks Tracker
Author: Joud Alnsour<br>
Date: 2022-05-11<br>
Application Version: 1.0.0<br>
Django: 4.0.4
## Steps to get started
- Run following CLI commands
     - poetry new [django-models]
     - poetry install
     - poetry shell
     - poetry add django
     - django-admin start project [snack_tracker_project]
     - python manage.py migrate
     - python manage.py createsuperuser
     - python manage.py startapp [snacks]
- Create your models, templates & views
- Run following CLI commands
     - python manage.py makemigrations
     - python manage.py migrate
## How to start the website 
- python manage.py runserver
- To view the snacks list, go to the url: 
>http://127.0.0.1:8000/snack-list