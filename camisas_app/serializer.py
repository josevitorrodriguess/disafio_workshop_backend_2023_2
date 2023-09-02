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
        # Define o modelo a ser serializado (Detalhes)
        model = Detalhes
        # Inclui todos os campos do modelo na serialização
        fields = '__all__'

    # Define um método personalizado para obter detalhes relacionados a uma camisa
    def get_detalhes(self, obj):
        # Filtra as camisas relacionadas ao objeto Detalhes
        detalhes = Camisa.objects.filter(camsisa=obj)
        
        # Usa o CamisaSerializer para serializar os detalhes das camisas encontradas
        detalhes_serializer = CamisaSerializer(detalhes, many=True)
        
        # Retorna os detalhes serializados como dados
        return detalhes_serializer.data