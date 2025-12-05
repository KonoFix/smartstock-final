from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_atual = models.IntegerField(default=0)
    quantidade_minima = models.IntegerField(default=5) # Gatilho do alerta

    def precisa_repor(self):
        return self.quantidade_atual <= self.quantidade_minima

    def __str__(self):
        return self.nome

class PedidoReposicao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    resolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"Repor: {self.produto.nome}"