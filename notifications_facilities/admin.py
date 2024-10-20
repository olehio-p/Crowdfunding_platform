from django.contrib import admin

from notifications_facilities.models.Notifications import Notification


# Register your models here.
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass