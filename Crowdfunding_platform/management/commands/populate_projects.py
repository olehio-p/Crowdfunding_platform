from datetime import date

from django.core.management.base import BaseCommand

from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.project_models.Category import Category

class Command(BaseCommand):
    help = 'Populate Project table'

    def handle(self, *args, **options):
        projects_data = [
            ('Smart Home Automation', 'An AI-powered smart home system that connects all your devices.', 100000.00, 45000.00, '2023-01-01', '2023-06-01', 1, 'active', 'tech, smart home, automation', 'https://www.example.com/video1'),
            ('Wearable Health Tracker', 'A lightweight health tracker with real-time data analysis.', 50000.00, 30000.00, '2023-02-15', '2023-07-15', 1, 'active', 'health, tech, wearable', 'https://www.example.com/video2'),
            ('Solar-Powered Charger', 'A portable solar charger for devices, perfect for camping.', 30000.00, 20000.00, '2023-03-01', '2023-08-01', 1, 'completed', 'solar, tech, charger', 'https://www.example.com/video3'),
            ('AI-Powered Personal Assistant', 'An AI assistant for scheduling, reminders, and everyday tasks.', 150000.00, 95000.00, '2023-02-01', '2023-07-01', 1, 'active', 'AI, tech, personal assistant', 'https://www.example.com/video4'),
            ('Home Fitness App', 'A mobile app that offers personalized fitness plans.', 50000.00, 25000.00, '2023-03-05', '2023-09-05', 2, 'active', 'fitness, app, health', 'https://www.example.com/video5'),
            ('Yoga Mat with Sensors', 'A yoga mat that tracks your posture and offers corrections.', 20000.00, 15000.00, '2023-04-15', '2023-10-15', 2, 'active', 'yoga, health, sensors', 'https://www.example.com/video6'),
            ('Fitness Tracker for Kids', 'A fun wearable fitness tracker designed specifically for children.', 30000.00, 15000.00, '2023-05-01', '2023-11-01', 2, 'active', 'fitness, kids, wearable', 'https://www.example.com/video7'),
            ('Educational Coding App', 'A gamified platform for kids to learn coding.', 75000.00, 40000.00, '2023-01-15', '2023-06-15', 3, 'active', 'education, coding, app', 'https://www.example.com/video8'),
            ('Interactive Science Kits', 'Hands-on science kits for kids to explore and learn.', 20000.00, 12000.00, '2023-02-20', '2023-08-20', 3, 'completed', 'science, education, kits', 'https://www.example.com/video9'),
            ('Language Learning App', 'A mobile app that helps users learn new languages interactively.', 50000.00, 30000.00, '2023-03-10', '2023-09-10', 3, 'active', 'language, education, app', 'https://www.example.com/video10'),
            ('Virtual Art Lessons', 'An online platform offering art lessons from professionals.', 25000.00, 18000.00, '2023-04-01', '2023-09-01', 3, 'active', 'art, education, lessons', 'https://www.example.com/video11'),
            ('Zero-Waste Grocery Store', 'A grocery store that offers zero-waste packaging options.', 100000.00, 60000.00, '2023-02-05', '2023-08-05', 6, 'active', 'zero waste, grocery, sustainability', 'https://www.example.com/video12'),
            ('Solar Energy Initiative', 'A project to bring solar energy solutions to rural areas.', 80000.00, 45000.00, '2023-01-25', '2023-07-25', 6, 'paused', 'solar, energy, environment', 'https://www.example.com/video13'),
            ('Eco-Friendly Packaging Solutions', 'A company offering eco-friendly alternatives to plastic packaging.', 75000.00, 50000.00, '2023-03-10', '2023-08-10', 6, 'active', 'eco-friendly, packaging, sustainability', 'https://www.example.com/video14'),
            ('Sustainable Clothing Line', 'A fashion line made from 100% recycled materials.', 50000.00, 30000.00, '2023-02-10', '2023-08-10', 5, 'active', 'fashion, sustainable, eco-friendly', 'https://www.example.com/video15'),
            ('Upcycled Fashion', 'Turning old clothes into trendy, new designs.', 30000.00, 15000.00, '2023-01-20', '2023-07-20', 5, 'active', 'fashion, upcycling, recycling', 'https://www.example.com/video16'),
            ('Fashion Accessories from Waste Materials', 'Fashion accessories made from repurposed materials.', 15000.00, 9000.00, '2023-03-05', '2023-09-05', 5, 'completed', 'fashion, accessories, recycling', 'https://www.example.com/video17'),
            ('Organic Vegan Restaurant', 'A vegan restaurant that uses only organic, locally-sourced ingredients.', 120000.00, 80000.00, '2023-04-01', '2023-10-01', 6, 'active', 'vegan, food, organic', 'https://www.example.com/video18'),
            ('Sustainable Coffee Shop', 'A coffee shop with a focus on fair trade and sustainability.', 80000.00, 50000.00, '2023-05-15', '2023-11-15', 6, 'active', 'coffee, fair trade, sustainability', 'https://www.example.com/video19'),
            ('Farm-to-Table Restaurant', 'A restaurant offering fresh, farm-to-table dishes.', 150000.00, 120000.00, '2023-01-10', '2023-07-10', 6, 'completed', 'food, farm-to-table, organic', 'https://www.example.com/video20'),
            ('Indie Film: The Road Less Traveled', 'A thought-provoking indie film about self-discovery.', 50000.00, 35000.00, '2023-02-15', '2023-08-15', 7, 'active', 'film, indie, self-discovery', 'https://www.example.com/video21'),
            ('Comic Book Series: Heroes Unmasked', 'An independent comic book series about a new breed of superheroes.', 30000.00, 22000.00, '2023-03-01', '2023-09-01', 20, 'active', 'comics, superheroes, action', 'https://www.example.com/video22'),
            ('Photography Book: Urban Jungle', 'A photography book that explores the beauty of urban landscapes.', 15000.00, 12000.00, '2023-04-10', '2023-09-10', 18, 'completed', 'photography, urban, book', 'https://www.example.com/video23'),
            ('Board Game: Battle of Legends', 'A strategic board game set in a fantasy world.', 60000.00, 40000.00, '2023-02-01', '2023-07-01', 8, 'active', 'games, board game, fantasy', 'https://www.example.com/video24'),
            ('Mobile Game: Kingdom Conquest', 'A mobile game where players build and conquer kingdoms.', 75000.00, 50000.00, '2023-03-05', '2023-09-05', 8, 'active', 'games, mobile, strategy', 'https://www.example.com/video25'),
            ('VR Experience: The Last Adventure', 'A VR experience that takes players on an epic journey.', 100000.00, 70000.00, '2023-04-20', '2023-10-20', 8, 'active', 'games, VR, adventure', 'https://www.example.com/video26'),
        ]

        for data in projects_data:
            project, created = Project.objects.get_or_create(
                title=data[0],
                description=data[1],
                goal_amount=data[2],
                current_amount=data[3],
                start_date=date.fromisoformat(data[4]),
                end_date=date.fromisoformat(data[5]),
                category=Category.objects.get(id=data[6]),
                status=data[7],
                tags=data[8],
                video_url=data[9]
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Project "{data[0]}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'Category "{data[0]}" already exists.'))
