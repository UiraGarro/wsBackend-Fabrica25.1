from django.urls import path
from .views import (
    home_view, PessoaListView, PessoaDetailView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView,
    TarefaListView, TarefaDetailView, TarefaCreateView, TarefaUpdateView, TarefaDeleteView,
    obter_dica
)

urlpatterns = [
    path('', home_view, name='home'),

    # Rotas para Pessoa
    path('pessoas/', PessoaListView.as_view(), name='listar_pessoas'),
    path('pessoas/<int:pk>/', PessoaDetailView.as_view(), name='detalhar_pessoa'),
    path('pessoas/criar/', PessoaCreateView.as_view(), name='criar_pessoa'),
    path('pessoas/editar/<int:pk>/', PessoaUpdateView.as_view(), name='editar_pessoa'),
    path('pessoas/deletar/<int:pk>/', PessoaDeleteView.as_view(), name='deletar_pessoa'),

    # Rotas para Tarefa
    path('tarefas/', TarefaListView.as_view(), name='listar_tarefas'),
    path('tarefas/<int:pk>/', TarefaDetailView.as_view(), name='detalhar_tarefa'),
    path('tarefas/criar/', TarefaCreateView.as_view(), name='criar_tarefa'),
    path('tarefas/editar/<int:pk>/', TarefaUpdateView.as_view(), name='editar_tarefa'),
    path('tarefas/deletar/<int:pk>/', TarefaDeleteView.as_view(), name='deletar_tarefa'),

    # API Externa
    path('dica/', obter_dica, name='obter_dica'),
]
