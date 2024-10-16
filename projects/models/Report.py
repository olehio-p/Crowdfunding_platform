from django.db import models
from django.utils import timezone

from projects.models import Project
from users.models import User


class Report(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='reports_made')
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
        db_table = 'report'
        indexes = [
            models.Index(fields=['reported_by']),
            models.Index(fields=['project']),
            models.Index(fields=['date']),
            models.Index(fields=['report_status']),
        ]

    def __str__(self):
        return f"Report ID: {self.id}, Status: {self.report_status}, Reported by: {self.reported_by}, Project: {self.project.title}"
