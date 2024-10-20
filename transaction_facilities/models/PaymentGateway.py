from django.db import models

class PaymentGateway(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    transaction_fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        managed = False
        db_table = 'payment_gateway'
        indexes = [
            models.Index(fields=['transaction_fee']),
        ]

