from django.db import models

# Define o modelo 'Camisa' que herda da classe 'models.Model'
class Camisa(models.Model):
    # Define um campo de texto para armazenar o nome do time
    time = models.CharField(max_length=20)
    
    # Define um campo de texto para armazenar o tipo de camisa (Goleiro, Treino, Jogo)
    tipo = models.CharField(max_length=20)

    # Define um método '__str__' que retorna uma representação de string legível do objeto
    def __str__(self):
        return f"Time: {self.time} Tipo(Goleiro, Treino, Jogo): {self.tipo}"

# Define o modelo 'Detalhes' que herda da classe 'models.Model'
class Detalhes(models.Model):
    # Define um campo de chave estrangeira para relacionar um objeto 'Detalhes' com um objeto 'Camisa'
    camisa = models.ForeignKey(Camisa, related_name='tipo_camisa', on_delete=models.CASCADE, null=True, blank=True)
    
    # Define um campo de texto para armazenar o nome
    nome = models.CharField(max_length=20)
    
    # Define um campo de texto para armazenar o tamanho
    tamanho = models.CharField(max_length=20)
    
    # Define um campo de texto para armazenar o número
    numero = models.CharField(max_length=5)

    # Define um método '__str__' que retorna uma representação de string legível do objeto
    def __str__(self):
        return f"Camisa : {self.camisa} Nome: {self.nome} Tamanho: {self.tamanho}  Número: {self.numero}"
