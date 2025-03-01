from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
import requests
from .models import Pessoa, Tarefa
from .forms import PessoaForm, TarefaForm

# 🏠 Página inicial
def home_view(request):
    return render(request, 'home.html')

# 📌 CRUD para Pessoa
class PessoaListView(ListView):
    model = Pessoa
    template_name = "pessoa_list.html"
    context_object_name = "pessoas"

class PessoaDetailView(DetailView):
    model = Pessoa
    template_name = "pessoa_detail.html"
    context_object_name = "pessoa"

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoa_form.html"
    success_url = reverse_lazy('listar_pessoas')

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoa_form.html"
    success_url = reverse_lazy('listar_pessoas')

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = "pessoa_confirm_delete.html"
    success_url = reverse_lazy('listar_pessoas')

# 📌 CRUD para Tarefa
class TarefaListView(ListView):
    model = Tarefa
    template_name = "tarefa_list.html"
    context_object_name = "tarefas"

class TarefaDetailView(DetailView):
    model = Tarefa
    template_name = "tarefa_detail.html"
    context_object_name = "tarefa"

class TarefaCreateView(CreateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = "tarefa_form.html"
    success_url = reverse_lazy('listar_tarefas')

class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = "tarefa_form.html"
    success_url = reverse_lazy('listar_tarefas')

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = "tarefa_confirm_delete.html"
    success_url = reverse_lazy('listar_tarefas')

# 🌍 Consumindo a API Advice Slip (Dica Aleatória)
def obter_dica(request):
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    if response.status_code == 200:
        dica = response.json()['slip']['advice']
    else:
        dica = "Não foi possível obter uma dica no momento."
    return render(request, 'dica.html', {'dica': dica})
