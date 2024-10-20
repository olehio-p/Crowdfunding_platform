from django.db import models

class Milestone(models.Model):
    project = models.ForeignKey('Project', models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    completion_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milestone'
