from rest_framework import serializers
from Crowdfunding_platform.models.project_models.Comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Comment
        fields = ['id', 'project', 'user', 'text', 'date']
        read_only_fields = ['id']