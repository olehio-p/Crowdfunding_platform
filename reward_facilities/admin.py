from django.contrib import admin

from reward_facilities.models.Reward import Reward

from reward_facilities.models.Reward_Claim import RewardClaim


# Register your models here.
@admin.register(Reward)
class RewardClaimAdmin(admin.ModelAdmin):
    pass


@admin.register(RewardClaim)
class RewardClaimAdmin(admin.ModelAdmin):
    pass