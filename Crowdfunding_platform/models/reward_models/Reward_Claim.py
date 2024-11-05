from django.db import models

from Crowdfunding_platform.models.reward_models.Reward import Reward
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser


class RewardClaim(models.Model):
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='reward_claims')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reward_claims')
    claim_date = models.DateTimeField(auto_now_add=True)
    is_fulfilled = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'reward_claim'
        unique_together = (('reward', 'user'),)
        indexes = [
            models.Index(fields=['reward']),
            models.Index(fields=['user']),
            models.Index(fields=['is_fulfilled', 'claim_date']),
        ]