from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Usuario

# Create your views here.

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    data = list(usuarios.values('id', 'nome', 'email', 'ativo', 'data_criacao'))
    return JsonResponse(data, safe=False)

def buscar_usuario_por_id(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    data = {
        'id': usuario.id,
        'nome': usuario.nome,
        'email': usuario.email,
        'ativo': usuario.ativo,
        'data_criacao': usuario.data_criacao,
    }
    return JsonResponse(data)
