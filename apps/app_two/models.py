from django.db import models
from datetime import date

# Create your models here.
class Items(models.Model):
    item_added = models.CharField(max_length = 45)
    item_created = models.CharField(max_length = 45)
    user = models.CharField(max_length = 255)
    action = models.CharField(max_length = 255)
    date_added = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
