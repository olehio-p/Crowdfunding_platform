from django.core.management.base import BaseCommand
from Crowdfunding_platform.models.user_models.Language import Language

class Command(BaseCommand):
    help = 'Populate the Language table with initial data'

    def handle(self, *args, **kwargs):
        languages = [
            {'code': 'en', 'name': 'English'},
            {'code': 'es', 'name': 'Spanish'},
            {'code': 'fr', 'name': 'French'},
            {'code': 'de', 'name': 'German'},
            {'code': 'zh', 'name': 'Chinese'},
            {'code': 'ja', 'name': 'Japanese'},
            {'code': 'ko', 'name': 'Korean'},
            {'code': 'ru', 'name': 'Russian'},
            {'code': 'pt', 'name': 'Portuguese'},
            {'code': 'ar', 'name': 'Arabic'},
            {'code': 'hi', 'name': 'Hindi'},
            {'code': 'it', 'name': 'Italian'},
            {'code': 'nl', 'name': 'Dutch'},
            {'code': 'sv', 'name': 'Swedish'},
            {'code': 'pl', 'name': 'Polish'},
            {'code': 'tr', 'name': 'Turkish'},
            {'code': 'no', 'name': 'Norwegian'},
            {'code': 'da', 'name': 'Danish'},
            {'code': 'fi', 'name': 'Finnish'},
            {'code': 'el', 'name': 'Greek'}
        ]

        for language_data in languages:
            Language.objects.get_or_create(code=language_data['code'], name=language_data['name'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the Language table.'))
