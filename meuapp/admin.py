from django.contrib import admin
from .models import Pessoa, Tarefa

admin.site.register(Pessoa)
admin.site.register(Tarefa)

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pessoa')
    search_fields = ('titulo', 'pessoa__nome')    
# Register your models here.
