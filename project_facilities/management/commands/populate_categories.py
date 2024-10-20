from django.core.management.base import BaseCommand
from project_facilities.models.Category import Category

class Command(BaseCommand):
    help = 'Populate Category table'

    def handle(self, *args, **options):
        categories_data = [
            ('Tech', 'Innovative tech gadgets, software, and hardware projects aiming to revolutionize industries.'),
            ('Health', 'Medical and health-related projects designed to improve well-being and healthcare.'),
            ('Education', 'Projects focused on improving education, creating learning tools, and expanding access to knowledge.'),
            ('Art', 'Creative art projects including music, painting, and digital artwork.'),
            ('Fashion', 'Unique clothing, accessories, and fashion-related projects for the style-conscious.'),
            ('Food', 'Culinary innovations, restaurants, and new food products.'),
            ('Film', 'Independent movies, documentaries, and visual storytelling projects seeking funding.'),
            ('Games', 'Video games, board games, and other gaming experiences in development.'),
            ('Music', 'Musicians, bands, and music projects aiming to record, produce, or perform.'),
            ('Publishing', 'Books, magazines, and other written media projects looking for support.'),
            ('Environment', 'Projects aimed at environmental conservation, renewable energy, and sustainability.'),
            ('Nonprofit', 'Social causes, charity projects, and initiatives to support communities in need.'),
            ('Sports', 'Sports events, new athletic gear, and fitness-related projects.'),
            ('Travel', 'Innovative travel experiences, adventure trips, and travel-related products.'),
            ('Design', 'Innovative product designs and creative solutions across multiple industries.'),
            ('Community', 'Local community projects and social initiatives to strengthen neighborhoods.'),
            ('Science', 'Scientific research, discoveries, and experiments seeking funding.'),
            ('Photography', 'Photography projects, exhibitions, and equipment aimed at professionals or enthusiasts.'),
            ('Theater', 'Theatrical productions, stage performances, and performing arts projects.'),
            ('Comics', 'Independent comic books, graphic novels, and manga projects seeking financial backing.'),
        ]

        for name, description in categories_data:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'description': description}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Category "{name}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Category "{name}" already exists.'))
