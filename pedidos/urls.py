from django.urls import path
from .views import cadastrar_pedido, lista_pedidos

urlpatterns = [
    path('cadastrar/', cadastrar_pedido, name='cadastrar_pedido'),
    path('', lista_pedidos, name='lista_pedidos'),
]