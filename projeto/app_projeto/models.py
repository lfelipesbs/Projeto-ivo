from django.db import models

class feedback(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.CharField(max_length=100)
    feedbacks = models.TextField(blank=True, null=True)

class atividades(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
