from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=70)
    card_id = models.CharField(max_length=70)


    def __str__(self):
        return self.card_id

