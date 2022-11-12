from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self): # Define o campo que aparecerá nas listas do admin ao invés do 'id'
        return self.nome
