from django.contrib import admin

from projects.models import Project, Category, Milestone, Update, Follower

admin.register(Category, Project, Milestone, Update, Follower)