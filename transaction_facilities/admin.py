from django.contrib import admin

from transaction_facilities.models.Dispute import Dispute

from transaction_facilities.models.Donation import Donation

from transaction_facilities.models.PaymentGateway import PaymentGateway

from transaction_facilities.models.Transaction import Transaction


# Register your models here.
@admin.register(Dispute)
class DonationAdmin(admin.ModelAdmin):
    pass


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentGateway)
class TransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass