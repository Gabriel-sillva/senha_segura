from rest_framework import serializers
from .models import HistoricoSenha

class HistoricoSenhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSenha
        fields = '__all__'