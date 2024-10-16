from django.contrib import admin

from projects.models import Project, Category, Milestone, Update, Follower, Report

admin.register(Category, Project, Milestone, Update, Follower, Report)