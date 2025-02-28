from django.shortcuts import render

import requests

from .models import filmes
from .config import OMDB_API_KEY

def buscar_filmes(request):
    query = request.GET.get('query')
    if query:
        url = f'http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={query}'
        response = requests.get(url)
        data = response.json()
        filmes = data.get('Search', [])
        for filme in filmes:
            filme_obj = filmes.objects.filter(título=filme['Title']).first()
            if filme_obj:
                filme['favorito'] = True
    else:
        filmes = []
        
    return render(request, 'filmes/buscar_filmes.html', {'filmes': filmes})