from django.urls import path
from .views import cadastrar_produto, lista_produtos

urlpatterns = [
    path('cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('', lista_produtos, name='lista_produtos'),
]