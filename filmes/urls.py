from django.urls import path

urlpatterns =   [
    path = ('', views.index, name='index'),
    path = ('filmes/', views.filmes, name='filmes'),
    path = ('buscar_filmes/', views.buscar_filmes, name='buscar_filmes'),
    path = ('favoritos/', views.favoritos, name='favoritos'),
]