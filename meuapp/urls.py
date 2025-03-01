from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('noticias/', views.noticias, name='noticias'),
    
]