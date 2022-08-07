from django.db import models

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        RECEIVED = 'RECEIVED', ('RECEIVED')
        CONFIRMED = 'CONFIRMED', ('CONFIRMED')
        DISPATCHED = 'DISPATCHED', ('DISPATCHED')
        DELIVERED = 'DELIVERED', ('DELIVERD')
        CANCELED = 'CANCELED', ('CANCELED')
   
    cliente = models.CharField(max_length=200)
    produto = models.CharField(max_length=200)
    valor = models.FloatField()
    entregue = models.BooleanField()
    estado = models.CharField(max_length=10, choices=OrderStatus.choices, blank=False, null=False, default='RECEIVED')
    timestamp = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.produto