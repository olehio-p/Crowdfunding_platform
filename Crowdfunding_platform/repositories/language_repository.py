from Crowdfunding_platform.repositories.base_repository import BaseRepository
from Crowdfunding_platform.models.user_models.Language import Language

class LanguageRepository(BaseRepository):
    def get(self, instance_id):
        return Language.objects.filter(id=instance_id).first()

    def get_all(self):
        return Language.objects.all()

    def create(self, **kwargs):
        return Language.objects.create(**kwargs)

    def update(self, instance_id, **kwargs):
        language = self.get(instance_id)
        if language:
            for key, value in kwargs.items():
                setattr(language, key, value)
            language.save()
            return language
        return None

    def delete(self, instance_id):
        language = self.get(instance_id)
        if language:
            language.delete()
            return True
        return False
