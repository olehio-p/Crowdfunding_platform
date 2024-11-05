from django.contrib.auth.models import User
from django.db import models

from Crowdfunding_platform.models.user_models.Language import Language
from Crowdfunding_platform.models.user_models.Location import Location


class CustomUser(models.Model):
    USER_TYPE_CHOICES = [
        ('creator', 'Creator'),
        ('backer', 'Backer'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.TextField(blank=True, null=True)
    bio = models.CharField(max_length=10000, blank=True, null=True)
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES, default=None, null=True, blank=True)
    join_date = models.DateField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    class Meta:
        managed = True
        db_table = 'user'

    def __str__(self):
        location_str = self.location.country if self.location else 'No Location'
        phone_str = self.phone_number if self.phone_number else 'No Phone'
        return (f"User: {self.user.username} | Email: {self.user.email} | "
                f"Type: {self.get_user_type_display()} | Phone: {phone_str} | "
                f"Location: {location_str}")