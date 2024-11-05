from rest_framework import serializers
from Crowdfunding_platform.models.project_models.Follower import Follower

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id', 'user', 'project', 'follow_date']
        read_only_fields = ['id']
