from django.db import models

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.transaction_models.Transaction import Transaction
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser


class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.RESTRICT, unique=True, related_name='donation')

    class Meta:
            managed = True
            db_table = 'donation'
            indexes = [
                models.Index(fields=['user']),
                models.Index(fields=['project']),
                models.Index(fields=['transaction']),
            ]

    def __str__(self):
        user_str = self.user.user.username if self.user else 'Anonymous'
        return (f"Donation of ${self.amount} by {user_str} to {self.project.title} "
                f"on {self.date.strftime('%Y-%m-%d')}")