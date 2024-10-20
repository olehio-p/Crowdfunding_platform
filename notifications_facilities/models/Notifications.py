from django.db import models

from project_facilities.models.Project import Project
from user_facilities.models.User import CustomUser


class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('donation', 'Donation'),
        ('project_update', 'Project Update'),
        ('reward', 'Reward'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=1000)
    type = models.CharField(max_length=15, choices=NOTIFICATION_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'notification'
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['project']),
            models.Index(fields=['created_at']),
        ]
