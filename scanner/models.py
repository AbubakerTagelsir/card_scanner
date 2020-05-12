from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=70)
    card_id = models.CharField(max_length=70)
    source_image = models.ImageField(max_length=None, null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name[:50]

