# wsBackend-Fabrica25.1

# Dicas Aleatórias 3000

## Descrição
O projeto "Dicas Aleatórias 3000" é uma aplicação web que fornece dicas aleatórias para os usuários. A aplicação é construída utilizando o framework Django para o backend e HTML para o frontend. A aplicação também integra a API Advice Slip para obter dicas aleatórias em inglês e utiliza a biblioteca `deep_translator` para traduzir essas dicas automaticamente para português antes de exibi-las aos usuários.

# Endpoints

### Endpoints para Pessoa
- **Listar Pessoas**: `GET /pessoas/` - Mapeado para `PessoaListView`
- **Detalhar Pessoa**: `GET /pessoas/<int:pk>/` - Mapeado para `PessoaDetailView`
- **Criar Pessoa**: `GET/POST /pessoas/criar/` - Mapeado para `PessoaCreateView`
- **Editar Pessoa**: `GET/POST /pessoas/editar/<int:pk>/` - Mapeado para `PessoaUpdateView`
- **Deletar Pessoa**: `POST /pessoas/deletar/<int:pk>/` - Mapeado para `PessoaDeleteView`

### Endpoints para Tarefa
- **Listar Tarefas**: `GET /tarefas/` - Mapeado para `TarefaListView`
- **Detalhar Tarefa**: `GET /tarefas/<int:pk>/` - Mapeado para `TarefaDetailView`
- **Criar Tarefa**: `GET/POST /tarefas/criar/` - Mapeado para `TarefaCreateView`
- **Editar Tarefa**: `GET/POST /tarefas/editar/<int:pk>/` - Mapeado para `TarefaUpdateView`
- **Deletar Tarefa**: `POST /tarefas/deletar/<int:pk>/` - Mapeado para `TarefaDeleteView`

### Endpoint para API Externa
- **Obter Dica**: `GET /dica/` - Mapeado para `obter_dica`

### Endpoint para Home
- **Home**: `GET /` - Mapeado para `home_view`

## Tecnologias Utilizadas
- **Backend:** Django
- **Frontend:** HTML, CSS
- **API Externa:** Advice Slip API
- **Tradução:** Biblioteca `deep_translator`
- **Banco de dados** MySqlcliente

## Estrutura do Projeto
- **Views:**
  - Funções para listar, criar, detalhar, editar e deletar pessoas e tarefas.
  - Função para obter dicas aleatórias traduzidas.
- **APIs:**
  - Integração com a API Advice Slip para obter dicas em inglês.
  - Uso da biblioteca `deep_translator` para traduzir dicas para português.

## Como Executar o Projeto
1. Clone o repositório do projeto:
- git clone https://github.com/UiraGarro/wsBackend-Fabrica25.1
- cd wsBackend-Fabrica25.1
2. Instale as dependências necessárias utilizando `pip install -r requirements.txt`.
3. Configure o banco de dados e execute as migrações do Django utilizando `python manage.py migrate`.
4. Inicie o servidor de desenvolvimento do Django utilizando `python manage.py runserver`.
5. Acesse a aplicação através do navegador no endereço [http://localhost:8000](http://localhost:8000).

## Dependências
As dependências do projeto estão listadas no arquivo `requirements.txt` e podem ser instaladas utilizando o comando `pip install -r requirements.txt`.