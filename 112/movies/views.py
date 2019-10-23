from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre

# Create your views here.
def index(request):
    #read data from DB
    genres = Genre.objects.all()
    items = ["Item1", "Red", "Coke", "Mouse"]
    # send data and render in html
    return render(request, 'views/index.html',{'title' : 'Index Page', 'items' : genres })
def welcome(request):
    return render(request, 'views/welcome.html')
def about(request):
    return HttpResponse("<h1> I am Travis</h1>")
def catalog(request):
    return render(request,'views/catalog.html')
