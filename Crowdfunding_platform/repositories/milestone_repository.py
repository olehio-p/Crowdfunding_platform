from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.project_models.Milestone import Milestone

class MilestoneRepository(BaseRepository):
    def get(self, instance_id):
        return Milestone.objects.filter(id=instance_id).first()

    def get_all(self):
        return Milestone.objects.all()

    def get_all_by_project(self, project_id):
        project = Project.objects.get(id=project_id)
        return Milestone.objects.filter(project=project)

    def create(self, **kwargs):
        return Milestone.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        milestone = self.get(instance_id)
        if milestone:
            for key, value in kwargs.items():
                setattr(milestone, key, value)
            milestone.save()
            return milestone
        return None

    def delete(self, instance_id):
        milestone = self.get(instance_id)
        if milestone:
            milestone.delete()
            return True
        return False
