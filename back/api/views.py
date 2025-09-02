from django.shortcuts import render
from rest_framework.decorators import api_view ### é usado para transformar funções normais do Django em views compatíveis com o Django REST Framework (DRF).
from rest_framework.response import response  ### a classe usada no Django REST Framework (DRF) para retornar respostas HTTP nas suas views.    
from .models import HistoricoSenha
from .serializers import HistoricoSenhaSerializers
import random, string, hashlib ### Esse import junta três módulos diferentes do Python padrão que são muito úteis quando você trabalha com geração de senhas, tokens ou qualquer tipo de hash:
 
                               ### random: Usado para gerar números ou escolhas aleatórias.

                               ### string: Fornece constantes de caracteres prontos, como letras e dígitos.

                               ### hashlib: Usado para criar hashes criptográficos (como MD5, SHA256).



### Gerar senha aleatória
@api_view(['GET'])
def gerar_senha(request):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(12))
    hash_senha = hashlib.sha1(senha.encode()).hexdigest()
    HistoricoSenha.objects.create(hash_senha=hash_senha)
    return response({'senha': senha})

### Verificar se senha já fi usada
@api_view(['POST'])
def verifcar_senha(request):
    senha = request.data.get('senha')
    if not senha:
        return response({'erro': 'Senha não informada'}, status=400)
    hash_senha = hashlib.sha1(senha.encode().hexdigest())
    vazada = HistoricoSenha.objects.filter(hash_senha=hash_senha).exists()
    return response({'vazada': vazada})


### listar Hisorico de senhar (hashadas)
@api_view(['GET'])
def listar_historico(request):
    historico = HistoricoSenha.objects.all()
    serializer = HistoricoSenhaSerializers(historico, many=True)
    return response(serializer.data)

### listar_historico mostra todos os registros de senhas hashadas, sem expor as senhas originais.