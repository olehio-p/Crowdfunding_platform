from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.transaction_models.Dispute import Dispute

class DisputeRepository(BaseRepository):
    def get(self, instance_id):
        return Dispute.objects.filter(id=instance_id).first()

    def get_all(self):
        return Dispute.objects.all()

    def create(self, **kwargs):
        return Dispute.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        dispute = self.get(instance_id)
        if dispute:
            for key, value in kwargs.items():
                setattr(dispute, key, value)
            dispute.save()
            return dispute
        return None

    def delete(self, instance_id):
        dispute = self.get(instance_id)
        if dispute:
            dispute.delete()
            return True
        return False
