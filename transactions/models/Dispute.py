from django.db import models
from django.utils import timezone

from transactions.models import Transaction
from users.models import User


class Dispute(models.Model):
    id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='disputes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disputes')
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('in review', 'In Review')
    ], default='open')
    created_at = models.DateTimeField(default=timezone.now)
    resolution_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'dispute'
        indexes = [
            models.Index(fields=['transaction']),
            models.Index(fields=['user']),
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Dispute {self.id} by {self.user.name} on transaction {self.transaction.id}"
