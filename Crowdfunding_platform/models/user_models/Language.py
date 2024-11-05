from django.db import models

class Language(models.Model):
    code = models.CharField(unique=True, max_length=10)
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'language'
