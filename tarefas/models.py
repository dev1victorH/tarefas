from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario_responsavel = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
