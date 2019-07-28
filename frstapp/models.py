from django.db import models
from django.utils import timezone
# Create your models here.

DATABASE_TYPES = (
    ('ORACLE','ORACLE_DATABASE'),
    ('SYBASE','SYBASE_DATABASE'),
)

class DModel(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField(max_length = 2000)
    driver = models.CharField(max_length = 100, choices = DATABASE_TYPES)
    host = models.CharField(max_length = 100)
    port = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)