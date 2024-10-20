from django.core.management.base import BaseCommand
from transaction_facilities.models.PaymentGateway import PaymentGateway

class Command(BaseCommand):
    help = 'Populate PaymentGateway table'

    def handle(self, *args, **options):
        gateways_data = [
            ('PayPal', 'active', 2.90),
            ('Stripe', 'active', 2.50),
            ('Square', 'active', 2.75),
            ('Authorize.Net', 'inactive', 2.95),
            ('WePay', 'inactive', 2.90),
            ('Payoneer', 'inactive', 2.00),
            ('Google Pay', 'active', 1.50),
            ('Amazon Pay', 'active', 3.00),
            ('2Checkout', 'inactive', 3.50),
            ('Apple Pay', 'active', 1.75),
        ]

        for name, status, transaction_fee in gateways_data:
            payment_gateway, created = PaymentGateway.objects.get_or_create(
                name=name,
                status=status,
                transaction_fee=transaction_fee
            )

        self.stdout.write(self.style.SUCCESS('Payment gateways populated successfully!'))
