from django.core.management.base import BaseCommand
from Crowdfunding_platform.models.user_models.Location import Location

class Command(BaseCommand):
    help = 'Populate the Location table with initial data'

    def handle(self, *args, **kwargs):
        locations = [
            {'country': 'USA', 'state': 'California', 'city': 'Los Angeles', 'postal_code': '90001'},
            {'country': 'USA', 'state': 'New York', 'city': 'New York', 'postal_code': '10001'},
            {'country': 'Canada', 'state': 'British Columbia', 'city': 'Vancouver', 'postal_code': 'V6B 1A1'},
            {'country': 'Australia', 'state': 'New South Wales', 'city': 'Sydney', 'postal_code': '2000'},
            {'country': 'Germany', 'state': None, 'city': 'Berlin', 'postal_code': '10178'},
            {'country': 'UK', 'state': 'England', 'city': 'London', 'postal_code': 'SW1A 1AA'},
            {'country': 'France', 'state': None, 'city': 'Paris', 'postal_code': '75001'},
            {'country': 'Japan', 'state': None, 'city': 'Tokyo', 'postal_code': '100-0001'},
            {'country': 'Italy', 'state': 'Lazio', 'city': 'Rome', 'postal_code': '00100'},
            {'country': 'Spain', 'state': 'Catalonia', 'city': 'Barcelona', 'postal_code': '08001'},
            {'country': 'Mexico', 'state': 'Distrito Federal', 'city': 'Mexico City', 'postal_code': '01000'},
            {'country': 'India', 'state': 'Maharashtra', 'city': 'Mumbai', 'postal_code': '400001'},
            {'country': 'Brazil', 'state': 'São Paulo', 'city': 'São Paulo', 'postal_code': '01000-000'},
            {'country': 'Russia', 'state': 'Moscow', 'city': 'Moscow', 'postal_code': '101000'},
            {'country': 'China', 'state': 'Beijing', 'city': 'Beijing', 'postal_code': '100000'},
            {'country': 'South Africa', 'state': 'Western Cape', 'city': 'Cape Town', 'postal_code': '8000'},
            {'country': 'Argentina', 'state': 'Buenos Aires', 'city': 'Buenos Aires', 'postal_code': 'C1000'},
            {'country': 'Netherlands', 'state': 'North Holland', 'city': 'Amsterdam', 'postal_code': '1011'},
            {'country': 'Sweden', 'state': 'Stockholm', 'city': 'Stockholm', 'postal_code': '11122'},
            {'country': 'South Korea', 'state': 'Seoul', 'city': 'Seoul', 'postal_code': '03000'},
        ]

        for location_data in locations:
            Location.objects.get_or_create(
                country=location_data['country'],
                state=location_data['state'],
                city=location_data['city'],
                postal_code=location_data['postal_code']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the Location table.'))
