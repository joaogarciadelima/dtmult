from rest_framework import serializers
from dtmult.propriedades.models import Propriedade


class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = ['id', 'nome', 'endereco', 'comentarios', 'slug', 'foto', 'multiproprietarios',
                  'tags', 'tipo_multipropriedade', 'data_cadastro']
