from django.contrib import admin

from projects.models import Project, Category, Milestone

admin.register(Project)
admin.register(Category)
admin.register(Milestone)