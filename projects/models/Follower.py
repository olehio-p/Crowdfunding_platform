from django.db import models
from django.utils import timezone

from projects.models import Project
from users.models import User


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='followers')
    follow_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'follower'
        unique_together = (('user', 'project'),)
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['project']),
            models.Index(fields=['follow_date']),
        ]

    def __str__(self):
        return f"{self.user.name} follows {self.project.title}"
