from rest_framework import serializers
from Crowdfunding_platform.models.user_models.Language import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code', 'name']
        read_only_fields = ['id']
