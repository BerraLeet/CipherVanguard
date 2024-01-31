# CipherVanguard

A basic Django deployment in Heroku

![cipher1](https://github.com/BerraLeet/CipherVanguard/assets/86689476/7b73f887-0265-4634-ba32-105f84ebfdea)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project CipherVanguard is about making people thats not into cybersecurity to start think about how vulnerable most of us are. I mostly post my other projects onto it, like my Password generator CryptWarden among others due to most people do not use or understand Github.

Also i im interrested to find like minded people into cybersecurity to connect and possibly collab later on. The Settings.py include some scurity features to prevent Cross-site-scripting and vulnerebilities from user sessions and also Redirects to only HTTPS traffic.

## Features

- Features a responsive navbar and uses load static to inherit base template
- Linked in and github buttons
- Media Quieries to make responsive design dynamically to fit all types of displays.

## Requirements

- Python 3
- venv
- Heroku CLI
- Github

## Installation

Create Django_project_folder

cd into it

Create a virtual environment
python -m venv env

cd env/Scripts

# Activate environment
inside env/Scripts run command:

    activate

    python.exe -m pip install --upgrade pip

    pip install -r requirements.txt

    django-admin startproject mysite

(env) cd mysite

## start server
(env) python manage.py runserver
http://127.0.0.1:8000/ or type localhost:8000 inside your webbrowser

## Generate new SECRET_KEY
    from django.core.management.utils import get_random_secret_key

    print(get_random_secret_key())
 
## Create environmentvariable .env
put Secret key in the .env and remember to turn DEBUG off before deployment
SECRET_KEY=your_goes_here
DEBUG=False

## Edit Settings.py
    from dotenv import load_dotenv
    
    load_dotenv()
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    DEBUG = os.environ.get('DEBUG') == 'True'
    
    STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

## Add your app
edit settings.py  
Installed_APPS
'main.apps.MainConfig'

(save settings) cmd 
python manage.py migrate

python manage.py makemigrations main

## Creates admin login
    python manage.py createsuperuser

## Collect static files
Create a folder  called static inside

    STATIC_URL = 'static/'

    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]

(env) python manage.py collectstatic



# Configuration

Create functions for each view in views.py example 

    from django.shortcuts import render

    from django.http import HttpResponse

    def home(request):

        return HttpResponse("Hello, this is the home page!")

    def about(request):

        return HttpResponse("Hello, this is the about page!")

also create urls corresponding to each view

    from django.urls import path

    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='about'),
    ]

### start developing : ) 
Experiment with HTML, CSS and Javascript.
i implemented Bootstrap 5 which comes with alot nice looking templates and cool features.


## Push to git

(bash) git init
(bash) git add .
(bash) git commit -m "Initial commit"


# Heroku setup
    pip install django-heroku

### Make Procfile

(bash) touch Procfile

(bash) nano Procfile

(Procfile)     web: gunicorn mysite.wsgi

## Edit settings.py
    import os

    import django_heroku

    import dj_database_url

    inside MIDDLEWARE [
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    django_heroku.settings(locals())

## Make commit and push git
(env) git add .

(env) git commit "Deployment Time"

(env) git push 

## Create SSH key
    ssh-keygen -t rsa -f ./my_key

## Heroku Deployment
heroku login

heroku keys:add
### Create project in heroku
heroku create

git push heroku (branch name)

Now its all setup! 

# Contributing
Feel free to contribute to this project. If you have suggestions or find issues, please open an issue or submit a pull request.

# Licence
This project is licensed under the MIT License.
