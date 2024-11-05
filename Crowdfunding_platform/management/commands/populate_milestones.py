from datetime import date

from django.core.management.base import BaseCommand

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.project_models.Milestone import Milestone

class Command(BaseCommand):
    help = 'Populate Milestone table'

    def handle(self, *args, **options):
        milestones_data = [
            (1, 'Prototype Development', 'Complete the initial prototype of the smart home system.', 25000.00, '2023-02-01'),
            (1, 'User Testing Phase', 'Conduct user testing to gather feedback and make improvements.', 15000.00, '2023-04-01'),
            (2, 'Design Finalization', 'Finalize the design of the wearable health tracker.', 10000.00, '2023-03-10'),
            (2, 'Manufacturing Start', 'Begin manufacturing of the first batch of devices.', 20000.00, None),
            (3, 'Material Sourcing', 'Source sustainable materials for the charger.', 5000.00, '2023-03-01'),
            (3, 'Production Start', 'Commence production of the solar-powered charger.', 10000.00, None),
            (5, 'MVP Development', 'Develop a minimum viable product (MVP) of the app.', 15000.00, '2023-03-15'),
            (5, 'Beta Testing', 'Launch beta testing for selected users.', 20000.00, '2023-07-01'),
            (8, 'Curriculum Development', 'Develop the curriculum for coding lessons.', 10000.00, '2023-01-30'),
            (8, 'Platform Launch', 'Launch the educational coding app to the public.', 30000.00, '2023-06-15'),
            (12, 'Location Secured', 'Secure a location for the grocery store.', 20000.00, '2023-03-01'),
            (12, 'Store Opening', 'Open the zero-waste grocery store to the public.', 30000.00, '2023-07-01'),
            (15, 'Fabric Sourcing', 'Source sustainable fabrics for clothing production.', 10000.00, '2023-02-01'),
            (15, 'Launch Collection', 'Launch the first collection of sustainable clothing.', 20000.00, '2023-06-01'),
            (18, 'Menu Development', 'Create the menu for the restaurant.', 15000.00, '2023-03-01'),
            (18, 'Grand Opening', 'Host the grand opening of the restaurant.', 30000.00, '2023-08-15'),
            (21, 'Casting Completed', 'Complete casting for the film.', 25000.00, '2023-02-20'),
            (21, 'Filming Completion', 'Finish filming the entire movie.', 30000.00, '2023-04-15'),
            (24, 'Game Design Finalization', 'Finalize the design and rules of the game.', 15000.00, '2023-05-01'),
            (24, 'Production of Game Pieces', 'Begin production of game pieces.', 20000.00, None),
            (23, 'Photography Collection', 'Complete the collection of photographs for the book.', 10000.00, '2023-06-01'),
            (23, 'Book Design', 'Design the layout and cover of the photography book.', 15000.00, '2023-08-01'),
        ]

        for data in milestones_data:
            milestone, created = Milestone.objects.get_or_create(
                project=Project.objects.get(id=data[0]),
                title=data[1],
                description=data[2],
                goal=data[3],
                completion_date=date.fromisoformat(data[4]) if data[4] else None
            )

        self.stdout.write(self.style.SUCCESS('Milestones populated successfully!'))
