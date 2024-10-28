from django.core.management.base import BaseCommand
from django.utils import timezone

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.project_models.Follower import Follower

from Crowdfunding_platform.models.user_models.CustomUser import CustomUser


class Command(BaseCommand):
    help = 'Populate Follower table'

    def handle(self, *args, **options):
        followers_data = [
            (3, 1, '2023-05-01 10:00:00'),
            (4, 1, '2023-05-05 11:30:00'),
            (5, 1, '2023-05-10 14:00:00'),
            (3, 2, '2023-06-01 09:45:00'),
            (6, 2, '2023-06-15 12:15:00'),
            (7, 2, '2023-06-20 16:00:00'),
            (4, 3, '2023-07-05 15:30:00'),
            (6, 3, '2023-07-10 13:00:00'),
            (5, 5, '2023-08-01 10:15:00'),
            (8, 5, '2023-08-10 12:30:00'),
            (6, 8, '2023-08-15 14:00:00'),
            (7, 8, '2023-08-20 09:30:00'),
            (8, 12, '2023-09-01 16:30:00'),
            (9, 12, '2023-09-05 11:00:00'),
            (7, 15, '2023-09-10 13:15:00'),
            (4, 15, '2023-09-12 10:45:00'),
            (9, 18, '2023-09-15 12:00:00'),
            (10, 18, '2023-09-20 14:00:00'),
            (6, 21, '2023-09-25 15:30:00'),
            (8, 21, '2023-09-28 10:00:00'),
            (5, 24, '2023-10-01 09:45:00'),
            (9, 24, '2023-10-05 14:15:00'),
        ]

        for user_id, project_id, follow_date in followers_data:
            follower, created = Follower.objects.get_or_create(
                user=CustomUser.objects.get(id=user_id),
                project=Project.objects.get(id=project_id),
                follow_date=timezone.datetime.strptime(follow_date, '%Y-%m-%d %H:%M:%S') if follow_date else timezone.now()
            )

        self.stdout.write(self.style.SUCCESS('Followers populated successfully!'))
