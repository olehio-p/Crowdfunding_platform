from typing import Any, Optional

from django.contrib.auth.models import User

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser


class CustomUserRepository(BaseRepository):
    def get(self, instance_id: int) -> Optional[CustomUser]:
        try:
            return CustomUser.objects.get(id=instance_id)
        except CustomUser.DoesNotExist:
            return None

    def get_all(self) -> list[CustomUser]:
        return CustomUser.objects.all()

    def get_all_by_country(self, country: str) -> list[CustomUser]:
        return CustomUser.objects.filter(location__country=country)

    def get_users_by_project(self, project_id):
        project = Project.objects.get(id=project_id)
        return CustomUser.objects.filter(followers__project=project)

    def create(self, username: str, password: str, **kwargs: Any) -> CustomUser:
        user = User(username=username, **kwargs)
        user.set_password(password)
        user.save()

        custom_user = CustomUser(user=user, join_date=kwargs.get('join_date'))
        custom_user.save()
        return custom_user

    def update(self, instance_id: int, **kwargs: Any) -> Optional[CustomUser]:
        try:
            custom_user = CustomUser.objects.get(id=instance_id)
            for key, value in kwargs.items():
                setattr(custom_user, key, value)
            custom_user.save()
            return custom_user
        except CustomUser.DoesNotExist:
            return None

    def delete(self, instance_id: int) -> bool:
        try:
            custom_user = CustomUser.objects.get(id=instance_id)
            custom_user.delete()
            return True
        except CustomUser.DoesNotExist:
            return False