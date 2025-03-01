# wsBackend-Fabrica25.1

# Dicas Aleatórias 3000

## Descrição
O projeto "Dicas Aleatórias 3000" é uma aplicação web que fornece dicas aleatórias para os usuários. A aplicação é construída utilizando o framework Django para o backend e HTML para o frontend. A aplicação também integra a API Advice Slip para obter dicas aleatórias em inglês e utiliza a biblioteca `deep_translator` para traduzir essas dicas automaticamente para português antes de exibi-las aos usuários.

## Funcionalidades
1. **Listar Pessoas:** Uma página que lista todas as pessoas cadastradas no sistema.
2. **Criar Pessoa:** Uma página que permite a criação de novos registros de pessoas.
3. **Detalhar Pessoa:** Uma página que exibe os detalhes de uma pessoa específica.
4. **Editar Pessoa:** Uma página que permite a edição dos dados de uma pessoa.
5. **Deletar Pessoa:** Uma página que permite a exclusão de uma pessoa.
6. **Listar Tarefas:** Uma página que lista todas as tarefas cadastradas no sistema.
7. **Criar Tarefa:** Uma página que permite a criação de novas tarefas.
8. **Detalhar Tarefa:** Uma página que exibe os detalhes de uma tarefa específica.
9. **Editar Tarefa:** Uma página que permite a edição dos dados de uma tarefa.
10. **Deletar Tarefa:** Uma página que permite a exclusão de uma tarefa.
11. **Dica Aleatória:** Uma página que exibe uma dica aleatória traduzida para português.

## Tecnologias Utilizadas
- **Backend:** Django
- **Frontend:** HTML, CSS
- **API Externa:** Advice Slip API
- **Tradução:** Biblioteca `deep_translator`

## Estrutura do Projeto
- **Templates:**
  - `home.html`: Página inicial que oferece opções para listar pessoas, criar pessoa, obter uma dica aleatória, listar tarefas e criar tarefa.
  - `pessoa_list.html`: Página que lista todas as pessoas cadastradas.
  - `pessoa_detail.html`: Página que exibe os detalhes de uma pessoa específica.
  - `pessoa_form.html`: Página para criar ou editar uma pessoa.
  - `pessoa_confirm_delete.html`: Página para confirmar a exclusão de uma pessoa.
  - `tarefa_list.html`: Página que lista todas as tarefas cadastradas.
  - `tarefa_detail.html`: Página que exibe os detalhes de uma tarefa específica.
  - `tarefa_form.html`: Página para criar ou editar uma tarefa.
  - `tarefa_confirm_delete.html`: Página para confirmar a exclusão de uma tarefa.
  - `dica.html`: Página que exibe uma dica aleatória traduzida para português.
- **Views:**
  - Funções para listar, criar, detalhar, editar e deletar pessoas e tarefas.
  - Função para obter dicas aleatórias traduzidas.
- **APIs:**
  - Integração com a API Advice Slip para obter dicas em inglês.
  - Uso da biblioteca `deep_translator` para traduzir dicas para português.

## Exemplo de Código
### home.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <h1>BEM-VINDO AO <strong>DICAS ALEATÓRIAS 3000</strong></h1>
    <h2>O QUE DESEJA FAZER?</h2>
    <ul>
        <li><a href="{% url 'listar_pessoas' %}">Listar Pessoas</a></li>
        <br>
        <li><a href="{% url 'criar_pessoa' %}">Criar Pessoa</a></li>
        <br>
        <li><a href="{% url 'obter_dica' %}">Dica Aleatória</a></li>
        <br>
        <li><a href="{% url 'listar_tarefas' %}">Listar Tarefas</a></li>
        <br>
        <li><a href="{% url 'criar_tarefa' %}">Criar Tarefa</a></li>
        <br>
    </ul>
</body>
</html>

Função para obter dica traduzida:

import requests
from deep_translator import GoogleTranslator

def obter_dica_traduzida():
    response = requests.get('https://api.adviceslip.com/advice')
    if response.status_code != 200:
        return "Erro ao obter dica."

    dica = response.json().get('slip', {}).get('advice', '')
    traducao = GoogleTranslator(source='auto', target='pt').translate(dica)
    return traducao

    Como Executar o Projeto:
1.Clone o repositório do projeto.
2.Instale as dependências necessárias utilizando pip install -r requirements.txt.
3.Configure o banco de dados e execute as migrações do Django utilizando python [manage.py](http://_vscodecontentref_/1) migrate.
4.Inicie o servidor de desenvolvimento do Django utilizando python [manage.py](http://_vscodecontentref_/2) runserver.
5.Acesse a aplicação através do navegador no endereço http://localhost:8000.

Dependências
As dependências do projeto estão listadas no arquivo requirements.txt e podem ser instaladas utilizando o comando pip install -r requirements.txt.