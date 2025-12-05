from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Produto, PedidoReposicao

@receiver(post_save, sender=Produto)
def checar_estoque(sender, instance, **kwargs):
    if instance.precisa_repor():
        # Verifica se já existe aviso pendente para não duplicar
        ja_existe = PedidoReposicao.objects.filter(produto=instance, resolvido=False).exists()
        
        if not ja_existe:
            PedidoReposicao.objects.create(produto=instance)
            print(f"⚠️ ALERTA: Pedido de reposição gerado para {instance.nome}")