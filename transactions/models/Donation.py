from django.db import models
from django.utils import timezone

from projects.models import Project
from users.models import User


class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    transaction_id = models.IntegerField(unique=True)

    class Meta:
        db_table = 'donation'
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['project']),
        ]

    def __str__(self):
        return f"Donation of {self.amount} for {self.project.title} by {self.user.name if self.user else 'Anonymous'} on {self.date}"
