from django.db import models
from django.utils import timezone

from transaction_facilities.models.Transaction import Transaction
from user_facilities.models.User import CustomUser


class Dispute(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='disputes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='disputes')
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('in review', 'In Review')
    ], default='open')
    created_at = models.DateTimeField(default=timezone.now)
    resolution_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'dispute'
        indexes = [
            models.Index(fields=['transaction']),
            models.Index(fields=['user']),
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['created_at']),
        ]
