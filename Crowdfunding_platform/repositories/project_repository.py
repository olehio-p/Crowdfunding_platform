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
