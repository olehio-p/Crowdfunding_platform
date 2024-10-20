from django.db import models

from crowdfunding_platform.project_facilities.models.Project import Project


class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestones')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    completion_date = models.DateField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'milestone'
