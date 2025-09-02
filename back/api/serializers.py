from rest_framework import serializers
from .models import HistoricoSenha

class HistoricoSenhaSerializers(serializers.ModelSerializer):
    class meta:
        model = HistoricoSenha
        fields = '__all__'