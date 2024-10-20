from django.contrib import admin

from user_facilities.models.User import CustomUser

from user_facilities.models.Language import Language

from user_facilities.models.Location import Location


# Register your models here.
@admin.register(CustomUser)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass