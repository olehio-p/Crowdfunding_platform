from decimal import Decimal
from typing import List, Dict, Any, Optional

import pandas as pd
from django.db.models import Count, QuerySet, Sum, Avg

from Crowdfunding_platform.models.project_models.Category import Category
from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.project_models.Project import Project

class ProjectRepository(BaseRepository):
    def get(self, instance_id):
        return Project.objects.filter(id=instance_id).first()

    def get_all(self):
        return Project.objects.all()

    def create(self, **kwargs):
        return Project.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        project = self.get(instance_id)
        if project:
            for key, value in kwargs.items():
                setattr(project, key, value)
            project.save()
            return project
        return None

    def delete(self, instance_id):
        project = self.get(instance_id)
        if project:
            project.delete()
            return True
        return False

    @staticmethod
    def convert_decimal_to_float(queryset: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [
            {k: float(v) if isinstance(v, Decimal) else v for k, v in item.items()}
            for item in queryset
        ]

    def get_all_projects(self,
                         category: Optional[str] = None,
                         start_date: Optional[str] = None,
                         end_date: Optional[str] = None) -> QuerySet:
        projects = Project.objects.all()

        if category and category != 'all':
            projects = projects.filter(category__name=category)

        if start_date:
            projects = projects.filter(donations__date__gte=start_date)

        if end_date:
            projects = projects.filter(donations__date__lte=end_date)

        return projects

    def get_donations_by_category(self, projects: QuerySet) -> List[Dict[str, Any]]:
        return list(
            projects.values("category__name")
            .annotate(total_donations=Sum("donations__amount"))
            .order_by("-total_donations")
        )

    def get_average_donation_by_category(self, projects: QuerySet) -> List[Dict[str, Any]]:
        return list(
            projects.values("category__name")
            .annotate(avg_donation=Avg("donations__amount"))
            .order_by("-avg_donation")
        )

    def get_donations_per_project(self, projects: QuerySet) -> List[Dict[str, Any]]:
        return list(
            projects.values("title")
            .annotate(
                total_donations=Sum("donations__amount"),
                donations_count=Count("donations__id"),
            )
            .order_by("-total_donations")
        )

    def get_followers_per_project(self, projects: QuerySet) -> List[Dict[str, Any]]:
        return list(
            projects.values("title")
            .annotate(total_followers=Count("followers__id"))
            .order_by("-total_followers")
        )

    def get_highest_goal_projects(self, projects: QuerySet) -> List[Dict[str, Any]]:
        return list(
            projects.values("title", "goal_amount")
            .order_by("-goal_amount")[:10]
        )

    def get_project_status_distribution(self, projects: QuerySet) -> List[Dict[str, Any]]:
        return list(
            projects.values("status")
            .annotate(status_count=Count("id"))
            .order_by("status")
        )

    def analyze_model_attributes(self, model_name: str, attributes: List[str]) -> Dict[str, Any]:
        if model_name == "Project":
            queryset = Project.objects.values(*attributes)
        elif model_name == "Category":
            queryset = Category.objects.values(*attributes)
        else:
            raise ValueError("Invalid model name")

        data = pd.DataFrame(list(queryset))
        return data.describe(include="all").to_dict()

    def get_model_attributes(self, model_name: str) -> List[str]:
        if model_name == "Project":
            return [field.name for field in Project._meta.get_fields()]
        elif model_name == "Category":
            return [field.name for field in Category._meta.get_fields()]
        else:
            raise ValueError("Invalid model name")
