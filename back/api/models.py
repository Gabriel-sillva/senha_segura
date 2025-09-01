from django.db import models

class HistoricoSenha(models.Model):
    hash_senha = models.CharField(max_length=128) ### CharField para o hash da senha. ###
    criada_em = models.DateTimeField(auto_now_add=True)  ###  DateTimeField(auto_now_add=True) salva automaticamente a data de criação.###

    def __str__(self):
        return self.hash_senha 
    
    ### O  __str__  serve para personalizar a forma como um objeto é exibido em texto.
# Create your models here.
