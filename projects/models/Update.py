from django.db import models
from django.utils import timezone

from projects.models import Project


class Update(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='updates')
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'update'
        indexes = [
            models.Index(fields=['project']),
            models.Index(fields=['date']),
        ]

    def __str__(self):
        return f"Update: {self.title} for {self.project.title} on {self.date}"
