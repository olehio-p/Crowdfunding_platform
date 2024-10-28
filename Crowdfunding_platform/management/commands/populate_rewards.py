from django.core.management.base import BaseCommand
from Crowdfunding_platform.models.reward_models.Reward import Reward
from Crowdfunding_platform.models.project_models.Project import Project


class Command(BaseCommand):
    help = 'Populate Reward table'

    def handle(self, *args, **options):
        rewards_data = [
            (1, 'Thank You!', 'A personalized thank you email and project updates.', 10.00, 100),
            (1, 'Early Bird Special', 'Receive a discount on your first order of our smart home devices.', 50.00, 50),
            (1, 'Exclusive Webinar', 'Join an exclusive webinar to learn about smart home technology.', 100.00, 25),
            (2, 'Get Fit!', 'A personalized thank you email and project updates.', 15.00, 150),
            (2, 'Health Tracker Discount', 'Receive a discount on the first wearable health tracker.', 60.00, 30),
            (2, 'Health Coach Session', 'One hour session with our health coach.', 200.00, 10),
            (3, 'Thank You!', 'A heartfelt thank you email and project updates.', 20.00, 200),
            (3, 'Charger Discount', 'Receive a discount on your first solar-powered charger.', 70.00, 75),
            (3, 'Exclusive T-Shirt', 'Get an exclusive T-shirt featuring our logo.', 150.00, 50),
            (5, 'Thank You!', 'A personalized thank you email and project updates.', 10.00, 100),
            (5, 'App Discount', 'Early access to the app and a discount on subscription.', 30.00, 200),
            (5, 'One-on-One Training', 'Receive a personalized training plan from a fitness coach.', 100.00, 25),
            (8, 'Thank You!', 'A personalized thank you email and project updates.', 10.00, 100),
            (8, 'Coding Bootcamp Discount', 'Get a discount on our coding bootcamp.', 40.00, 50),
            (8, 'Early Access', 'Gain early access to the app before it launches.', 80.00, 30),
            (12, 'Thank You!', 'A personalized thank you email and project updates.', 20.00, 150),
            (12, 'Gift Card', 'Receive a gift card to our grocery store.', 50.00, 75),
            (12, 'Exclusive Membership', 'Become a member with special discounts.', 100.00, 50),
            (15, 'Thank You!', 'A personalized thank you email and project updates.', 15.00, 200),
            (15, 'Clothing Discount', 'Get a discount on your first purchase.', 50.00, 100),
            (15, 'Limited Edition Item', 'Receive a limited edition clothing item.', 150.00, 30),
            (18, 'Thank You!', 'A personalized thank you email and project updates.', 25.00, 100),
            (18, 'Meal Voucher', 'Get a voucher for a free meal at our restaurant.', 50.00, 50),
            (18, 'Cooking Class', 'Join a cooking class to learn about vegan recipes.', 100.00, 20),
            (21, 'Thank You!', 'A personalized thank you email and project updates.', 10.00, 200),
            (21, 'Movie Screening', 'Receive an invitation to the exclusive screening.', 30.00, 75),
            (21, 'Behind-the-Scenes Access', 'Get exclusive behind-the-scenes content.', 100.00, 30),
            (24, 'Thank You!', 'A personalized thank you email and project updates.', 10.00, 100),
            (24, 'Game Copy', 'Receive a copy of the game when it is released.', 50.00, 200),
            (24, 'Designer Meet-Up', 'Meet the game designers and play an early version.', 150.00, 15),
        ]

        for project_id, title, description, min_donation, limit in rewards_data:
            reward, created = Reward.objects.get_or_create(
                project=Project.objects.get(id=project_id),
                title=title,
                description=description,
                min_donation=min_donation,
                limit=limit
            )

        self.stdout.write(self.style.SUCCESS('Rewards populated successfully!'))
