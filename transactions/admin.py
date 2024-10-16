from django.contrib import admin

from transactions.models import Transaction
from transactions.models.PaymentGateway import PaymentGateway

admin.register(Transaction, PaymentGateway)
