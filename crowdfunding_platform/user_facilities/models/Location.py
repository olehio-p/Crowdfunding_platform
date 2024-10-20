from django.db import models

class Location(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'location'
