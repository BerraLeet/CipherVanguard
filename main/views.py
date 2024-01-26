from django.shortcuts import render
from django.http import HttpResponse
from . models import ToDOList, Item

def index(response):
    #ls = ToDOList.objects.get(id=id)
    return render(response,"main/base.html", {})

def home(response):
    return render(response,"main/home.html", {})

def projects(response):
    return render(response,"main/projects.html", {})

def blog(response):
    return render(response,"main/blog.html", {})

def lifestyle(response):
    return render(response,"main/lifestyle.html", {})
