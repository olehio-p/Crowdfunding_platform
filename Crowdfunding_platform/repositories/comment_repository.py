from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.project_models.Comment import Comment

class CommentRepository(BaseRepository):
    def get(self, instance_id):
        return Comment.objects.filter(id=instance_id).first()

    def get_all(self):
        return Comment.objects.all()

    def get_all_by_project(self, project_id):
        project = Project.objects.get(id=project_id)
        return Comment.objects.filter(project=project)

    def create(self, **kwargs):
        return Comment.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        comment = self.get(instance_id)
        if comment:
            for key, value in kwargs.items():
                setattr(comment, key, value)
            comment.save()
            return comment
        return None

    def delete(self, instance_id):
        comment = self.get(instance_id)
        if comment:
            comment.delete()
            return True
        return False
