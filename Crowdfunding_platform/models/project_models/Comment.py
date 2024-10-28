from django.db import models

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'comment'
        indexes = [
            models.Index(fields=['project']),
            models.Index(fields=['user']),
            models.Index(fields=['date']),
        ]