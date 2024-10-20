from django.db import models
from django.utils import timezone

from crowdfunding_platform.project_facilities.models.Project import Project
from crowdfunding_platform.transaction_facilities.models.Transaction import Transaction
from crowdfunding_platform.user_facilities.models.User import CustomUser


class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.RESTRICT, unique=True, related_name='donation')

    class Meta:
            managed = False
            db_table = 'donation'
            indexes = [
                models.Index(fields=['user']),
                models.Index(fields=['project']),
                models.Index(fields=['transaction']),
            ]
