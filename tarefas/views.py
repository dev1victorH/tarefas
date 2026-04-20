from django.shortcuts import render
from django.http import JsonResponse
from .models import Tarefa

# Create your views here.

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().select_related('usuario_responsavel')
    data = []
    for tarefa in tarefas:
        tarefa_data = {
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'concluida': tarefa.concluida,
            'data_criacao': tarefa.data_criacao,
            'usuario_responsavel': tarefa.usuario_responsavel.nome if tarefa.usuario_responsavel else None,
        }
        data.append(tarefa_data)
    return JsonResponse(data, safe=False)
