from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.project_models.Category import Category

class CategoryRepository(BaseRepository):
    def get(self, instance_id):
        return Category.objects.filter(id=instance_id).first()

    def get_all(self):
        return list(Category.objects.all())

    def create(self, **kwargs):
        return Category.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        category = self.get(instance_id)
        if category:
            for key, value in kwargs.items():
                setattr(category, key, value)
            category.save()
            return category
        return None

    def delete(self, instance_id):
        category = self.get(instance_id)
        if category:
            category.delete()
            return True
        return False
