from django.contrib import admin

from projects.models import Project, Category, Milestone, Update

admin.register(Category, Project, Milestone, Update)