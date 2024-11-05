from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.transaction_models.Transaction import Transaction

class TransactionRepository(BaseRepository):
    def get(self, instance_id):
        return Transaction.objects.filter(id=instance_id).first()

    def get_all(self):
        return Transaction.objects.all()

    def create(self, **kwargs):
        return Transaction.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        transaction = self.get(instance_id)
        if transaction:
            for key, value in kwargs.items():
                setattr(transaction, key, value)
            transaction.save()
            return transaction
        return None

    def delete(self, instance_id):
        transaction = self.get(instance_id)
        if transaction:
            transaction.delete()
            return True
        return False
