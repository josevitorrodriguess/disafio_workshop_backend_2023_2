from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import Camisa, Detalhes
from .serializer import CamisaSerializer, DetalhesSerializer

# Viewset para o modelo Camisa
class CamisaViewset(viewsets.ModelViewSet):
    queryset = Camisa.objects.all()
    serializer_class = CamisaSerializer
    pagination_class = LimitOffsetPagination # Define a paginação usando LimitOffsetPagination

# Viewset para o modelo Detalhes
class DetalhesViewset(viewsets.ModelViewSet):
    queryset = Detalhes.objects.all()
    serializer_class = DetalhesSerializer
    pagination_class = LimitOffsetPagination  # Define a paginação usando LimitOffsetPagination