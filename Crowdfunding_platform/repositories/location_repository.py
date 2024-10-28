from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.user_models.Location import Location

class LocationRepository(BaseRepository):
    def get(self, instance_id):
        return Location.objects.filter(id=instance_id).first()

    def get_all(self):
        return Location.objects.all()

    def create(self, **kwargs):
        return Location.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        location = self.get(instance_id)
        if location:
            for key, value in kwargs.items():
                setattr(location, key, value)
            location.save()
            return location
        return None

    def delete(self, instance_id):
        location = self.get(instance_id)
        if location:
            location.delete()
            return True
        return False
