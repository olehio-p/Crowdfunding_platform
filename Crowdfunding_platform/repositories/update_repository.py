from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.project_models.Update import Update

class UpdateRepository(BaseRepository):
    def get(self, instance_id):
        return Update.objects.filter(id=instance_id).first()

    def get_all(self):
        return Update.objects.all()

    def get_all_by_project(self, project_id):
        project = Project.objects.get(id=project_id)
        return Update.objects.filter(project=project)

    def create(self, **kwargs):
        return Update.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        update = self.get(instance_id)
        if update:
            for key, value in kwargs.items():
                setattr(update, key, value)
            update.save()
            return update
        return None

    def delete(self, instance_id):
        update = self.get(instance_id)
        if update:
            update.delete()
            return True
        return False
