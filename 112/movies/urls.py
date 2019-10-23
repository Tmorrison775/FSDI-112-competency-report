from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="root"),
    path('welcome', views.welcome, name="welcome"),
    path('movies', views.index, name="index"),
    path('about', views.about, name="about"),
    path('index', views.index, name="index"),
    path('catalog',views.catalog, name="catalog")
]