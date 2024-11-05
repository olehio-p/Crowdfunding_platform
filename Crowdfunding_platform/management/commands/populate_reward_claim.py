from django.core.management.base import BaseCommand
from Crowdfunding_platform.models.reward_models.Reward_Claim import RewardClaim
from Crowdfunding_platform.models.reward_models.Reward import Reward
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser


class Command(BaseCommand):
    help = 'Populate RewardClaim table'

    def handle(self, *args, **options):
        claims_data = [
            (1, 3, '2023-05-02 10:00:00', True),
            (2, 4, '2023-05-06 11:30:00', False),
            (3, 5, '2023-05-12 14:00:00', True),
            (4, 6, '2023-06-02 09:45:00', False),
            (5, 3, '2023-06-16 12:15:00', True),
            (6, 8, '2023-06-21 16:00:00', True),
            (7, 9, '2023-07-06 15:30:00', True),
            (8, 10, '2023-07-11 13:00:00', False),
            (9, 5, '2023-08-02 10:15:00', True),
            (10, 4, '2023-08-11 12:30:00', False),
            (11, 6, '2023-08-13 13:00:00', True),
            (12, 7, '2023-08-16 14:00:00', True),
            (13, 9, '2023-08-22 09:30:00', False),
            (14, 10, '2023-08-25 12:00:00', True),
            (15, 8, '2023-09-02 16:30:00', True),
            (16, 7, '2023-09-07 11:00:00', True),
            (17, 5, '2023-09-12 14:15:00', False),
            (18, 6, '2023-09-15 12:00:00', True),
            (19, 3, '2023-09-17 10:45:00', True),
            (20, 4, '2023-09-19 13:00:00', False),
            (21, 10, '2023-09-22 14:30:00', True),
            (22, 9, '2023-09-24 10:00:00', True),
            (23, 8, '2023-09-28 15:15:00', False),
            (24, 2, '2023-09-29 09:45:00', True),
            (25, 7, '2023-09-30 11:00:00', False),
            (26, 3, '2023-10-02 10:30:00', True),
            (27, 5, '2023-10-04 13:15:00', True),
            (28, 1, '2023-10-06 14:45:00', False),
            (29, 6, '2023-10-07 15:30:00', True),
            (30, 2, '2023-10-08 16:00:00', False),
        ]

        for reward_id, user_id, claim_date, is_fulfilled in claims_data:
            RewardClaim.objects.get_or_create(
                reward=Reward.objects.get(id=reward_id),
                user=CustomUser.objects.get(id=user_id),
                claim_date=claim_date,
                is_fulfilled=is_fulfilled
            )

        self.stdout.write(self.style.SUCCESS('Reward claims populated successfully!'))
