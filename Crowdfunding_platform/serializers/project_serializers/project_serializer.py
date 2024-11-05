from rest_framework import serializers
from Crowdfunding_platform.models.project_models.Project import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'goal_amount',
            'current_amount', 'start_date', 'end_date',
            'category', 'status', 'project_image',
            'tags', 'video_url', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id']
