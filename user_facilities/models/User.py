from django.contrib.auth.models import User
from django.db import models

from user_facilities.models import Language, Location


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
