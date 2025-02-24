from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=255)
    profissao = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo
