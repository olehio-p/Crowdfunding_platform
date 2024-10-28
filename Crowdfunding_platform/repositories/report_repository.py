from Crowdfunding_platform.models import CustomUser
from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.project_models.Report import Report

class ReportRepository(BaseRepository):
    def get(self, instance_id):
        return Report.objects.filter(id=instance_id).first()

    def get_all(self):
        return Report.objects.all()

    def get_all_by_project(self, project_id):
        project = Project.objects.get(id=project_id)
        return Report.objects.filter(project=project)

    def get_all_by_user(self, user_id):
        user = CustomUser.objects.get(id=user_id)
        return Report.objects.filter(reported_by=user)

    def create(self, **kwargs):
        return Report.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        report = self.get(instance_id)
        if report:
            for key, value in kwargs.items():
                setattr(report, key, value)
            report.save()
            return report
        return None

    def delete(self, instance_id):
        report = self.get(instance_id)
        if report:
            report.delete()
            return True
        return False
