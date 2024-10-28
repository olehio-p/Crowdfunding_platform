from django.core.management.base import BaseCommand
from django.utils import timezone

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.project_models.Report import Report
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser


class Command(BaseCommand):
    help = 'Populate Report table'

    def handle(self, *args, **options):
        reports_data = [
            (3, 1, 'Suspicious activity related to funding sources.', '2023-06-18 12:30:00', 'pending'),
            (4, 2, 'Inappropriate content in project updates.', '2023-06-22 14:00:00', 'resolved'),
            (5, 3, 'Misleading information about product features.', '2023-06-30 09:15:00', 'pending'),
            (6, 4, 'Project failed to deliver promised rewards.', '2023-07-05 10:45:00', 'dismissed'),
            (7, 5, 'Fake reviews and ratings submitted.', '2023-07-15 08:20:00', 'pending'),
            (8, 6, 'Unclear terms regarding shipping and refunds.', '2023-07-20 11:30:00', 'resolved'),
            (9, 7, 'Project owner not responding to inquiries.', '2023-07-25 14:50:00', 'pending'),
            (10, 8, 'Inaccurate project timeline provided.', '2023-08-01 13:30:00', 'resolved'),
            (11, 9, 'Unauthorized use of copyrighted materials.', '2023-08-05 09:45:00', 'pending'),
            (12, 10, 'Lack of transparency in financials.', '2023-08-10 15:00:00', 'dismissed'),
            (13, 1, 'Violation of platform terms of service.', '2023-08-15 16:45:00', 'pending'),
            (14, 2, 'Claims of false achievements.', '2023-08-20 14:30:00', 'resolved'),
            (15, 3, 'Delayed delivery with no communication.', '2023-08-25 12:15:00', 'pending'),
            (16, 4, 'Harassment of users in comment section.', '2023-08-30 17:00:00', 'resolved'),
            (17, 5, 'Suspicion of fraudulent activity.', '2023-09-01 10:00:00', 'pending'),
        ]

        for reported_by_id, project_id, reason, date0, report_status in reports_data:
            report, created = Report.objects.get_or_create(
                reported_by=CustomUser.objects.get(id=reported_by_id),
                project=Project.objects.get(id=project_id),
                reason=reason,
                date=timezone.datetime.strptime(date0, '%Y-%m-%d %H:%M:%S'),
                report_status=report_status
            )

        self.stdout.write(self.style.SUCCESS('Reports populated successfully!'))
