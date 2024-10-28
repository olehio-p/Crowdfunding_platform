from rest_framework import serializers
from Crowdfunding_platform.models.project_models.Report import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'reported_by', 'project', 'reason', 'date', 'report_status']
        read_only_fields = ['id']