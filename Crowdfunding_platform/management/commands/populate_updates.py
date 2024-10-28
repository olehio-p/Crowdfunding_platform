from django.core.management.base import BaseCommand
from django.utils import timezone

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.project_models.Update import Update


class Command(BaseCommand):
    help = 'Populate Update table'

    def handle(self, *args, **options):
        updates_data = [
            (1, 'Prototype Completed', 'We have successfully completed the prototype and are moving into user testing.', '2023-02-10 10:00:00'),
            (1, 'User Testing Started', 'User testing has commenced, and we are gathering valuable feedback.', '2023-03-01 14:30:00'),
            (2, 'Design Review', 'The design has been reviewed, and final adjustments are being made.', '2023-03-15 09:00:00'),
            (2, 'First Batch Ready', 'The first batch of wearable health trackers is now ready for shipping.', '2023-04-10 11:15:00'),
            (3, 'Sourcing Materials', 'We have sourced sustainable materials and are ready for production.', '2023-02-20 12:00:00'),
            (3, 'Production Progress', 'Production is progressing smoothly, with the first units expected next week.', '2023-03-25 08:45:00'),
            (5, 'Beta Version Released', 'The beta version of the app has been released to selected users for feedback.', '2023-05-05 13:00:00'),
            (5, 'Feature Improvements', 'Based on feedback, we are implementing several feature improvements.', '2023-06-15 15:30:00'),
            (8, 'Curriculum Complete', 'The curriculum for our coding lessons has been completed and is ready for launch.', '2023-04-20 16:00:00'),
            (8, 'Public Launch Announcement', 'We are excited to announce the public launch of our educational coding app!', '2023-07-01 09:30:00'),
            (12, 'Location Secured', 'We have secured a prime location for our grocery store!', '2023-03-05 10:30:00'),
            (12, 'Renovation Progress', 'Renovation is underway, and we anticipate opening soon.', '2023-04-12 14:00:00'),
            (15, 'Fabric Arrived', 'The sustainable fabrics for our first collection have arrived!', '2023-02-28 11:00:00'),
            (15, 'Production Phase', 'Production of our first clothing line is officially underway!', '2023-05-10 09:15:00'),
            (18, 'Menu Finalized', 'Our menu has been finalized, featuring exciting new dishes!', '2023-05-20 13:30:00'),
            (18, 'Staff Training', 'Staff training is in progress to ensure excellent service upon opening.', '2023-06-05 12:00:00'),
            (21, 'Filming Started', 'Filming has started, and we are on schedule for completion.', '2023-04-15 08:00:00'),
            (21, 'Post-Production Begins', 'Post-production work has begun, and we’re excited to share our film soon!', '2023-07-10 10:45:00'),
            (24, 'Game Mechanics Finalized', 'The game mechanics have been finalized after extensive testing.', '2023-03-30 15:00:00'),
            (24, 'Prototype Testing', 'We are currently testing prototypes with focus groups for feedback.', '2023-05-25 11:30:00'),
            (23, 'Photo Collection Complete', 'We have completed our photo collection for the Urban Jungle book.', '2023-06-20 14:00:00'),
            (23, 'Design Phase Started', 'We have started the design phase for the book layout.', '2023-07-15 09:00:00'),
        ]

        for project_id, title, content, date in updates_data:
            update, created = Update.objects.get_or_create(
                project=Project.objects.get(id=project_id),
                title=title,
                content=content,
                date=timezone.datetime.strptime('2023-09-01 10:00:00', '%Y-%m-%d %H:%M:%S')
            )

        self.stdout.write(self.style.SUCCESS('Updates populated successfully!'))
