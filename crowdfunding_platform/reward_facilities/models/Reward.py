from django.db import models

from crowdfunding_platform.project_facilities.models.Project import Project


class Reward(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True, blank=True)
    min_donation = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    limit = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'reward'
        indexes = [
            models.Index(fields=['project']),
        ]
