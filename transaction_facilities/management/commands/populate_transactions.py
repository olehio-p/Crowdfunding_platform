from django.core.management.base import BaseCommand
from project_facilities.models.Project import Project
from transaction_facilities.models.PaymentGateway import PaymentGateway
from user_facilities.models.User import CustomUser
from transaction_facilities.models.Transaction import Transaction

class Command(BaseCommand):
    help = 'Populate Transaction table'

    def handle(self, *args, **options):
        transactions_data = [
            (3, 1, 'donation', 100.00, 1, '2023-06-15 10:30:00', 'completed'),
            (4, 2, 'donation', 50.00, 2, '2023-06-20 11:45:00', 'completed'),
            (5, 3, 'donation', 75.00, 1, '2023-06-25 14:00:00', 'completed'),
            (6, 4, 'donation', 120.00, 3, '2023-07-01 15:30:00', 'completed'),
            (7, 5, 'donation', 200.00, 4, '2023-07-10 12:00:00', 'completed'),
            (8, 6, 'donation', 80.00, 5, '2023-07-15 09:00:00', 'completed'),
            (9, 7, 'donation', 95.00, 1, '2023-07-20 13:45:00', 'completed'),
            (10, 8, 'donation', 150.00, 2, '2023-07-25 14:30:00', 'completed'),
            (3, 9, 'donation', 60.00, 3, '2023-08-01 16:15:00', 'completed'),
            (4, 10, 'donation', 85.00, 4, '2023-08-05 17:00:00', 'completed'),
            (1, 1, 'fee', 10.00, 1, '2023-06-15 10:35:00', 'completed'),
            (2, 2, 'fee', 5.00, 2, '2023-06-20 11:50:00', 'completed'),
            (3, 3, 'fee', 7.50, 1, '2023-06-25 14:05:00', 'completed'),
            (4, 4, 'fee', 12.00, 3, '2023-07-01 15:35:00', 'completed'),
            (5, 5, 'fee', 20.00, 4, '2023-07-10 12:05:00', 'completed'),
            (2, 1, 'withdrawal', 90.00, 2, '2023-06-18 14:45:00', 'completed'),
            (6, 2, 'withdrawal', 45.00, 3, '2023-06-25 12:00:00', 'completed'),
            (8, 3, 'withdrawal', 67.50, 5, '2023-06-29 09:30:00', 'completed'),
            (9, 4, 'withdrawal', 108.00, 1, '2023-07-05 10:00:00', 'completed'),
            (10, 5, 'withdrawal', 180.00, 4, '2023-07-15 11:00:00', 'completed'),
            (3, 6, 'donation', 100.00, 1, '2023-07-20 10:30:00', 'failed'),
            (4, 7, 'donation', 150.00, 2, '2023-07-25 13:45:00', 'failed'),
            (5, 8, 'donation', 175.00, 1, '2023-08-01 12:30:00', 'pending'),
            (6, 9, 'donation', 50.00, 3, '2023-08-05 11:15:00', 'pending'),
            (7, 10, 'donation', 90.00, 4, '2023-08-10 13:00:00', 'pending'),
            (8, 1, 'withdrawal', 85.00, 5, '2023-08-12 10:45:00', 'pending'),
            (9, 2, 'withdrawal', 45.00, 1, '2023-08-15 12:30:00', 'pending'),
            (11, 6, 'donation', 110.00, 1, '2023-07-25 15:30:00', 'completed'),
            (12, 7, 'donation', 130.00, 2, '2023-07-26 16:00:00', 'completed'),
            (13, 8, 'donation', 95.00, 3, '2023-07-28 17:30:00', 'completed'),
            (14, 9, 'donation', 125.00, 4, '2023-07-30 18:00:00', 'completed'),
            (15, 10, 'donation', 75.00, 5, '2023-08-01 19:00:00', 'completed'),
            (16, 1, 'donation', 90.00, 1, '2023-08-02 14:00:00', 'completed'),
            (17, 2, 'donation', 100.00, 2, '2023-08-03 14:30:00', 'completed'),
            (18, 3, 'donation', 115.00, 3, '2023-08-05 15:00:00', 'completed'),
            (19, 4, 'donation', 135.00, 4, '2023-08-07 15:30:00', 'completed'),
            (20, 5, 'donation', 145.00, 5, '2023-08-10 16:00:00', 'completed'),
            (11, 6, 'fee', 11.00, 1, '2023-07-25 15:35:00', 'completed'),
            (12, 7, 'fee', 13.00, 2, '2023-07-26 16:05:00', 'completed'),
            (13, 8, 'fee', 9.50, 3, '2023-07-28 17:35:00', 'completed'),
            (14, 9, 'fee', 12.50, 4, '2023-07-30 18:05:00', 'completed'),
            (15, 10, 'fee', 7.50, 5, '2023-08-01 19:05:00', 'completed'),
            (16, 1, 'withdrawal', 81.00, 1, '2023-08-03 13:30:00', 'completed'),
            (17, 2, 'withdrawal', 90.00, 2, '2023-08-05 12:00:00', 'completed'),
            (18, 3, 'withdrawal', 103.50, 3, '2023-08-07 13:45:00', 'completed'),
            (19, 4, 'withdrawal', 121.50, 4, '2023-08-10 15:00:00', 'completed'),
            (20, 5, 'withdrawal', 130.50, 5, '2023-08-12 14:30:00', 'completed'),
        ]

        for user_id, project_id, type, amount, payment_gateway_id, date, status in transactions_data:
            transaction, create = Transaction.objects.get_or_create(
                user=CustomUser.objects.get(id=user_id),
                project=Project.objects.get(id=project_id),
                type=type,
                amount=amount,
                payment_gateway=PaymentGateway.objects.get(id=payment_gateway_id),
                date=date,
                status=status
            )

        self.stdout.write(self.style.SUCCESS('Transactions populated successfully!'))
