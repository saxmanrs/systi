from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    usuario = models.CharField(max_length=30)
    setor = models.CharField(max_length=25)
    inicio = models.DateField('Data Inicio')
    saida = models.DateField('Data de Saida', null = True)
    pc = models.CharField(max_length = 5)
    cargo = models.CharField(max_length = 30)


    def __str__(self):
        return self.nome


