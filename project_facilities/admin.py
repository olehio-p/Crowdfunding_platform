from django.contrib import admin

from project_facilities.models.Category import Category

from project_facilities.models.Comment import Comment

from project_facilities.models.Follower import Follower

from project_facilities.models.Milestone import Milestone

from project_facilities.models.Project import Project

from project_facilities.models.Report import Report

from project_facilities.models.Update import Update


# Register your models here.
@admin.register(Category)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Follower)
class MilestoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ReportAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    pass