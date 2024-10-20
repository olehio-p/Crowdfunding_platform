from django.db import models
from django.utils import timezone

from crowdfunding_platform.project_facilities.models.Project import Project
from crowdfunding_platform.user_facilities.models.User import CustomUser


class Follower(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='followers')
    follow_date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'follower'
        unique_together = (('user', 'project'),)
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['project']),
            models.Index(fields=['follow_date']),
        ]
