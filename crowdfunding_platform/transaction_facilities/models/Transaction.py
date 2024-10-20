from django.db import models
from django.utils import timezone

from crowdfunding_platform.project_facilities.models.Project import Project
from crowdfunding_platform.transaction_facilities.models.PaymentGateway import PaymentGateway
from crowdfunding_platform.user_facilities.models.User import CustomUser


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
        managed = False
        db_table = 'transaction'
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['project']),
            models.Index(fields=['date']),
            models.Index(fields=['status', 'date']),
        ]
