from django.db import models
from django.utils import timezone

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser


class Follower(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followers')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='followers')
    follow_date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'follower'
        unique_together = (('user', 'project'),)
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['project']),
            models.Index(fields=['follow_date']),
        ]
