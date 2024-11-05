from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category'

    def __str__(self):
        return self.name