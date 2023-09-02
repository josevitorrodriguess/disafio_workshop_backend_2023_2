from rest_framework import routers
from .views import CamisaViewSet, DetalhesViewSet

# Cria um objeto de roteador padrão do Django REST framework
router = routers.DefaultRouter()

# Registra os viewsets 'CamisaViewSet' e 'DetalhesViewSet' no roteador
router.register(r'camisas', CamisaViewSet)
router.register(r'detalhes', DetalhesViewSet)

# Obtém as URLs geradas pelo roteador e as armazena em 'urlpatterns'
urlpatterns = router.urls
