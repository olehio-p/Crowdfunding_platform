from rest_framework import serializers
from Crowdfunding_platform.models.project_models.Milestone import Milestone

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ['id', 'project', 'title', 'description', 'goal', 'completion_date']
        read_only_fields = ['id']
