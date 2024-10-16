from django.db import models

class Location(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['country'], name='idx_location_country'),
            models.Index(fields=['city'], name='idx_location_city'),
        ]
        db_table = 'location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return f"{self.city}, {self.country} ({self.postal_code})"

