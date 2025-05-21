from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from pedidos.models import Pedido


@shared_task
def task_atualizar_estoque(pedido_id):
    pedido = Pedido.objects.filter(id=pedido_id).first()
    if not pedido:
        result = f'Pedido {pedido_id} não encontrado!'
        print(result)
        return result
    produto = pedido.produto
    produto.estoque -= pedido.quantidade
    produto.save()
    result = f"Estoque atualizado para o produto {produto.nome}: {produto.estoque}"
     
    if send_mail(
        f'Novo pedido realizado | ID {pedido.id}',
        f'Um novo pedido foi realizado:\n\nProduto: {produto.nome}\nQuantidade: {pedido.quantidade}\nEstoque atual: {produto.estoque}',
        settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_PEDIDO_DESTINO],
        fail_silently=False,
    ):
        result += '\nEmail enviado para ' + settings.EMAIL_PEDIDO_DESTINO
    print(result)
    return result