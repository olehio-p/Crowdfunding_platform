from django.db import models

from project_facilities.models.Category import Category


class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('paused', 'Paused'),
    ]

    title = models.CharField(max_length=45)
    description = models.TextField(max_length=10000)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='projects')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    project_image = models.BinaryField(null=True, blank=True)
    tags = models.CharField(max_length=500, null=True, blank=True)
    video_url = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'project'