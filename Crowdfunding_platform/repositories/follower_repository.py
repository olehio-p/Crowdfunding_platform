from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.project_models.Follower import Follower


class FollowerRepository(BaseRepository):
    def get(self, instance_id):
        return Follower.objects.filter(id=instance_id).first()

    def get_all(self):
        return Follower.objects.all()

    def create(self, **kwargs):
        return Follower.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        follower = self.get(instance_id)
        if follower:
            for key, value in kwargs.items():
                setattr(follower, key, value)
            follower.save()
            return follower
        return None

    def delete(self, instance_id):
        follower = self.get(instance_id)
        if follower:
            follower.delete()
            return True
        return False
