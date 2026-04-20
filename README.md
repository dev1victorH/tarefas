# Projeto Tarefas e Usuários

Este projeto Django implementa um sistema de tarefas com usuários responsáveis.

## Funcionalidades

- Gerenciamento de usuários (nome, email, status ativo)
- Gerenciamento de tarefas com atribuição a usuários
- APIs REST para listar usuários e tarefas
- Interface de administração Django

## Endpoints

- GET /usuarios/ - Lista todos os usuários
- GET /usuarios/<id>/ - Busca usuário por ID
- GET /tarefas/ - Lista todas as tarefas com nome do usuário responsável

## Como executar

1. Instalar dependências: `pip install -r requirements.txt`
2. Executar migrações: `python manage.py migrate`
3. Executar servidor: `python manage.py runserver`

## GitHub

O código está disponível em: https://github.com/dev1victorH/tarefas.git