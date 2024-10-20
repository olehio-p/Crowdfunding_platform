from django.core.management.base import BaseCommand
from transaction_facilities.models.Dispute import Dispute
from user_facilities.models.User import CustomUser
from transaction_facilities.models.Transaction import Transaction

class Command(BaseCommand):
    help = 'Populate Dispute table'

    def handle(self, *args, **options):
        dispute_data = [
            (1, 3, 'Transaction amount was charged twice.', 'in review', '2023-06-20 12:00:00', None),
            (2, 4, 'The payment gateway did not process correctly.', 'closed', '2023-06-25 13:30:00', '2023-06-28 15:00:00'),
            (3, 5, 'I was charged the wrong amount.', 'open', '2023-07-01 09:45:00', None),
            (21, 3, 'Failed donation still shows pending in my account.', 'closed', '2023-07-22 16:30:00', '2023-07-25 10:30:00'),
            (22, 4, 'Transaction failed, but amount was deducted.', 'open', '2023-07-30 14:30:00', None),
            (11, 8, 'Withdrawal request was canceled without reason.', 'in review', '2023-08-01 11:00:00', None),
            (12, 9, 'Amount withdrawn differs from the expected amount.', 'closed', '2023-08-05 10:15:00', '2023-08-08 16:00:00'),
            (13, 10, 'Payment gateway issue during withdrawal.', 'open', '2023-08-10 13:00:00', None),
            (23, 5, 'Pending donation still not processed after several days.', 'open', '2023-08-12 14:30:00', None),
            (24, 6, 'Payment still pending, but I received a confirmation email.', 'in review', '2023-08-14 12:00:00', None),
            (14, 11, 'Incorrect amount charged during the donation.', 'open', '2023-08-17 10:00:00', None),
            (15, 12, 'Transaction shows success, but the funds were not received.', 'open', '2023-08-20 09:45:00', None),
            (16, 13, 'Unauthorized transaction detected.', 'closed', '2023-08-22 15:00:00', '2023-08-24 10:30:00'),
        ]

        for transaction_id, user_id, reason, status, created_at, resolution_date in dispute_data:
            dispute, create = Dispute.objects.get_or_create(
                transaction=Transaction.objects.get(id=transaction_id),
                user=CustomUser.objects.get(id=user_id),
                reason=reason,
                status=status,
                created_at=created_at,
                resolution_date=resolution_date,
            )

        self.stdout.write(self.style.SUCCESS('Disputes populated successfully!'))
