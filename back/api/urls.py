from django.urls import path
from .views import gerar_senha, verifcar_senha, listar_historico

urlpatterns = [
    
path('gerar_senha/', gerar_senha, name='gerar_senha'),

path('verificar_senha/', verifcar_senha, name='verificar_senha'),

path('historico/', listar_historico, name='listar_historico'),

]