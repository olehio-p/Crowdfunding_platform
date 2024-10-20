from django.db import models
import Category

class Project(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=10000)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    status = models.CharField(max_length=9)
    project_image = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=500, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'