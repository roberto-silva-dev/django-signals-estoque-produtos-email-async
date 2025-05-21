from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from pedidos.models import Pedido
from pedidos.tasks import task_atualizar_estoque


@receiver(post_save, sender=Pedido)
def signal_atualizar_estoque(sender, instance, created, **kwargs):
    if created:
        def disparar_task():
            celery_task = task_atualizar_estoque.apply_async((instance.id,), countdown=1)
            if celery_task and celery_task.id:
                print(f'Task agendada para atualização de estoque {celery_task.id}')

        transaction.on_commit(disparar_task)
