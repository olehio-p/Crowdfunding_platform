from django.db import models

from crowdfunding_platform.project_facilities.models.Project import Project


class Analytics(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='analytics')
    total_views = models.IntegerField(default=0)
    total_donations = models.IntegerField(default=0)
    total_funds = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'analytics'
        indexes = [
            models.Index(fields=['total_views']),
            models.Index(fields=['total_funds', 'total_donations']),
        ]