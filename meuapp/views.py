from django.shortcuts import render, redirect
from .forms import NewsForm
import requests
import json
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            return redirect('noticias')
    else:
        form = NewsForm()
    return render(request, 'meupp/home.html', {'form': form})

def noticias(request):
    api_key = '2mvJdRxugj7l2hkfYH1km03v5Mosgmfv'
    url = f'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        news = response.json().get('resultados', [])
        return render(request, 'noticias.html', {'news': news})
    else:
        messages.error(request, 'Erro ao acessar a API do NY Times')
        return redirect('home')