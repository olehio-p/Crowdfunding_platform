from django.db import models
from django.utils import timezone

from project_facilities.models.Project import Project
from user_facilities.models.User import CustomUser


class Report(models.Model):
    reported_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='reports_made')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reports')
    reason = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    report_status = models.CharField(
        max_length=10,
        choices=[
            ('pending', 'Pending'),
            ('resolved', 'Resolved'),
            ('dismissed', 'Dismissed'),
        ],
        default='pending',
    )

    class Meta:
        managed = True
        db_table = 'report'
        indexes = [
            models.Index(fields=['reported_by']),
            models.Index(fields=['project']),
            models.Index(fields=['date']),
            models.Index(fields=['report_status']),
        ]