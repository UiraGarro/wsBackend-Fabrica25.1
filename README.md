# wsBackend-Fabrica25.1

# Dicas Aleatórias 3000

## Descrição
O projeto "Dicas Aleatórias 3000" é uma aplicação web que fornece dicas aleatórias para os usuários. A aplicação é construída utilizando o framework Django para o backend e HTML para o frontend. A aplicação também integra a API Advice Slip para obter dicas aleatórias em inglês e utiliza a biblioteca `deep_translator` para traduzir essas dicas automaticamente para português antes de exibi-las aos usuários.

## Funcionalidades
1. **Listar Pessoas:** Uma página que lista todas as pessoas cadastradas no sistema.
2. **Criar Pessoa:** Uma página que permite a criação de novos registros de pessoas.
3. **Dica Aleatória:** Uma página que exibe uma dica aleatória traduzida para português.

## Tecnologias Utilizadas
- **Backend:** Django
- **Frontend:** HTML, CSS
- **API Externa:** Advice Slip API
- **Tradução:** Biblioteca `deep_translator`

## Estrutura do Projeto
- **Templates:**
  - `home.html`: Página inicial que oferece opções para listar pessoas, criar pessoa e obter uma dica aleatória.
- **Views:**
  - Funções para listar pessoas, criar pessoa e obter dicas aleatórias.
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
        <li><a href="{% url 'criar_pessoa' %}">Criar Pessoa</a></li>
        <li><a href="{% url 'obter_dica' %}">Dica Aleatória</a></li>
    </ul>
</body>
</html>

Função para obter dica traduzida

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
3.Configure o banco de dados e execute as migrações do Django.
4.Inicie o servidor de desenvolvimento do Django.
5.Acesse a aplicação através do navegador no endereço http://localhost:8000.