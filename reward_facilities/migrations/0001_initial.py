# Generated by Django 5.1.2 on 2024-10-20 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("project_facilities", "0001_initial"),
        ("user_facilities", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reward",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "description",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "min_donation",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("limit", models.IntegerField(blank=True, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rewards",
                        to="project_facilities.project",
                    ),
                ),
            ],
            options={
                "db_table": "reward",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="RewardClaim",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("claim_date", models.DateTimeField(auto_now_add=True)),
                ("is_fulfilled", models.BooleanField(default=False)),
                (
                    "reward",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reward_claims",
                        to="reward_facilities.reward",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reward_claims",
                        to="user_facilities.customuser",
                    ),
                ),
            ],
            options={
                "db_table": "reward_claim",
                "managed": True,
            },
        ),
        migrations.AddIndex(
            model_name="reward",
            index=models.Index(fields=["project"], name="reward_project_5d7d5d_idx"),
        ),
        migrations.AddIndex(
            model_name="rewardclaim",
            index=models.Index(
                fields=["reward"], name="reward_clai_reward__7beed4_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="rewardclaim",
            index=models.Index(fields=["user"], name="reward_clai_user_id_489224_idx"),
        ),
        migrations.AddIndex(
            model_name="rewardclaim",
            index=models.Index(
                fields=["is_fulfilled", "claim_date"],
                name="reward_clai_is_fulf_bfeacf_idx",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="rewardclaim",
            unique_together={("reward", "user")},
        ),
    ]
