from rest_framework import serializers
from Crowdfunding_platform.models.project_models.Category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']