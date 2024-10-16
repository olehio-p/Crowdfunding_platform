from django.contrib import admin

from transactions.models import Transaction, Donation
from transactions.models.PaymentGateway import PaymentGateway

admin.register(Transaction, PaymentGateway, Donation)
