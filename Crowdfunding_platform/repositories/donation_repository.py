from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.transaction_models.Donation import Donation

class DonationRepository(BaseRepository):
    def get(self, instance_id):
        return Donation.objects.filter(id=instance_id).first()

    def get_all(self):
        return Donation.objects.all()

    def create(self, **kwargs):
        return Donation.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        donation = self.get(instance_id)
        if donation:
            for key, value in kwargs.items():
                setattr(donation, key, value)
            donation.save()
            return donation
        return None

    def delete(self, instance_id):
        donation = self.get(instance_id)
        if donation:
            donation.delete()
            return True
        return False
