from django.contrib import admin

from projects.models import Project, Category, Milestone

admin.register(Category, Project, Milestone)