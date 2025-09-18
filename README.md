# Teste Técnico – Sistema de Cadastro de Currículos

## Objetivo do Teste

Este projeto foi desenvolvido como uma solução para um teste técnico, com o objetivo de demonstrar habilidades em desenvolvimento web full-stack utilizando o framework Django. A tarefa consistia em criar um sistema de gerenciamento de currículos (CRUD - Create, Read, Update, Delete) com dois perfis de usuário: o candidato, que submete suas informações, e o recrutador, que gerencia e avalia os perfis cadastrados.

## Funcionalidades

* **Página de Acesso**: Uma página inicial que direciona os usuários para a área de candidatura ou para a área de recrutador.
* **Formulário de Cadastro**: Um formulário completo para os candidatos inserirem seus dados, incluindo:
    * Dados Pessoais
    * Contato
    * Experiência Profissional
    * Formação Acadêmica
* **Visualização de Candidatos**: Uma lista de todos os candidatos cadastrados, acessível para recrutadores autenticados.
* **Detalhes do Candidato**: Visualização detalhada de todas as informações de um candidato específico.
* **CRUD de Candidatos**: Recrutadores podem criar, visualizar, atualizar e deletar (CRUD) os perfis dos candidatos.
* **Autenticação de Recrutadores**: Sistema de login para que apenas usuários autorizados tenham acesso à lista de candidatos.

## Tecnologias Utilizadas

* **Backend**: Python, Django
* **Frontend**: HTML, CSS, Bootstrap
* **Banco de Dados**: SQLite3

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/projetopegho.git](https://github.com/seu-usuario/projetopegho.git)
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd projetopegho
    ```
3.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```
4.  **Instale as dependências:**
    ```bash
    pip install Django
    ```
5.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```
6.  **Crie um superusuário para acessar a área de administração e a área de recrutador:**
    ```bash
    python manage.py createsuperuser
    ```
7.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
8.  Acesse a aplicação em `http://127.0.0.1:8000/`.

## Estrutura do Projeto

* `mysite/`: Contém as configurações do projeto Django.
* `form/`: A aplicação principal do projeto, que contém os modelos, views, formulários e templates relacionados ao sistema de currículos.
* `static/`: Armazena arquivos estáticos como CSS e imagens.
* `db.sqlite3`: O banco de dados SQLite do projeto.
* `manage.py`: O script de linha de comando do Django para gerenciar o projeto.
