from django.db import models
from languages.models import Language
from locations.models import Location

class User(models.Model):
    USER_TYPE_CHOICES = [
        ('creator', 'Creator'),
        ('backer', 'Backer'),
        ('admin', 'Admin'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=45, unique=True)
    password_hash = models.CharField(max_length=45)
    profile_picture = models.BinaryField(null=True, blank=True)
    bio = models.TextField(max_length=10000, null=True, blank=True)
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES, default=None, null=True, blank=True)
    join_date = models.DateField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    def __str__(self):
        return self.name
