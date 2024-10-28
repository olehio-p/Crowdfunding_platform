from rest_framework import serializers
from Crowdfunding_platform.models.project_models.Update import Update

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ['id', 'project', 'title', 'content', 'date']
        read_only_fields = ['id']
