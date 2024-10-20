from django.db import models
from django.utils import timezone

from project_facilities.models.Project import Project


class Update(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='updates')
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'update'
        indexes = [
            models.Index(fields=['project']),
            models.Index(fields=['date']),
        ]
