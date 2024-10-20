from django.contrib import admin

from analytics_facilities.models.Analytics import Analytics


# Register your models here.
@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    pass