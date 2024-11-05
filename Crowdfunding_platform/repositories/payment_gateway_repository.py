from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.transaction_models.PaymentGateway import PaymentGateway

class PaymentGatewayRepository(BaseRepository):
    def get(self, instance_id):
        return PaymentGateway.objects.filter(id=instance_id).first()

    def get_all(self):
        return PaymentGateway.objects.all()

    def create(self, **kwargs):
        return PaymentGateway.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        paymentGateway = self.get(instance_id)
        if paymentGateway:
            for key, value in kwargs.items():
                setattr(paymentGateway, key, value)
            paymentGateway.save()
            return paymentGateway
        return None

    def delete(self, instance_id):
        paymentGateway = self.get(instance_id)
        if paymentGateway:
            paymentGateway.delete()
            return True
        return False
