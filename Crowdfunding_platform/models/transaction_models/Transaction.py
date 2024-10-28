from django.db import models
from django.utils import timezone

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.transaction_models.PaymentGateway import PaymentGateway
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('donation', 'Donation'),
        ('fee', 'Fee'),
        ('withdrawal', 'Withdrawal'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transactions')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_gateway = models.ForeignKey(PaymentGateway, null=True, blank=True, on_delete=models.SET_NULL, related_name='transactions')
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        managed = True
        db_table = 'transaction'
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['project']),
            models.Index(fields=['date']),
            models.Index(fields=['status', 'date']),
        ]
