from django.contrib import admin
from django.urls import path, include

# Lista de padrões de URL do aplicativo
urlpatterns = [
    # Define um padrão de URL para acessar a interface de administração do Django
    path('admin/', admin.site.urls),
    
    # Define um padrão de URL para incluir as URLs do aplicativo 'camisas_app'
    path('camisas_app', include('camisas_app.urls'))
]
