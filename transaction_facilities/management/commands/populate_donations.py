from django.core.management.base import BaseCommand
from project_facilities.models.Project import Project
from transaction_facilities.models.Donation import Donation
from user_facilities.models.User import CustomUser
from transaction_facilities.models.Transaction import Transaction

class Command(BaseCommand):
    help = 'Populate Donation table'

    def handle(self, *args, **options):
        donation_data = [
            (1, 3, 100.00, '2023-06-15 10:30:00', 1),
            (2, 4, 50.00, '2023-06-20 11:45:00', 2),
            (3, 5, 75.00, '2023-06-25 14:00:00', 3),
            (4, 6, 120.00, '2023-07-01 15:30:00', 4),
            (5, 7, 200.00, '2023-07-10 12:00:00', 5),
            (6, 8, 80.00, '2023-07-15 09:00:00', 6),
            (7, 9, 95.00, '2023-07-20 13:45:00', 7),
            (8, 10, 150.00, '2023-07-25 14:30:00', 8),
            (9, 3, 60.00, '2023-08-01 16:15:00', 9),
            (10, 4, 85.00, '2023-08-05 17:00:00', 10),
            (6, 3, 100.00, '2023-07-20 10:30:00', 21),
            (7, 4, 150.00, '2023-07-25 13:45:00', 22),
            (8, 5, 175.00, '2023-08-01 12:30:00', 23),
            (9, 6, 50.00, '2023-08-05 11:15:00', 24),
            (10, 7, 90.00, '2023-08-10 13:00:00', 25),
            (6, 11, 110.00, '2023-07-25 15:30:00', 31),
            (7, 12, 130.00, '2023-07-26 16:00:00', 32),
            (8, 13, 95.00, '2023-07-28 17:30:00', 33),
            (9, 14, 125.00, '2023-07-30 18:00:00', 34),
            (10, 15, 75.00, '2023-08-01 19:00:00', 35),
            (1, 16, 90.00, '2023-08-02 14:00:00', 36),
            (2, 17, 100.00, '2023-08-03 14:30:00', 37),
            (3, 18, 115.00, '2023-08-05 15:00:00', 38),
            (4, 19, 135.00, '2023-08-07 15:30:00', 39),
            (5, 20, 145.00, '2023-08-10 16:00:00', 40),
        ]

        for project_id, user_id, amount, date, transaction_id in donation_data:
            donation, create = Donation.objects.get_or_create(
                project=Project.objects.get(id=project_id),
                user=CustomUser.objects.get(id=user_id),
                amount=amount,
                date=date,
                transaction=Transaction.objects.get(id=transaction_id)
            )

        self.stdout.write(self.style.SUCCESS('Donations populated successfully!'))
