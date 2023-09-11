from rest_framework import serializers
from .models import Camisa, Detalhes

# Define um serializador chamado CamisaSerializer
class CamisaSerializer(serializers.ModelSerializer):
    class Meta:
        # Define o modelo a ser serializado (Camisa)
        model = Camisa
        # Inclui todos os campos do modelo na serialização
        fields = '__all__'

# Define um serializador chamado DetalhesSerializer
class DetalhesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalhes
        fields = '__all__'
    
    def get_detalhes(self, obj):
        detalhes = Camisa.objects.filter(camsisa=obj)
        detalhes_serializer = CamisaSerializer(detalhes, many=True)
        return detalhes_serializer.data