from rest_framework import serializers
from Crowdfunding_platform.models.user_models.Location import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'country', 'state', 'city', 'postal_code']
        read_only_fields = ['id']
