from django.db import models

class Card(models.Model):
    card_number = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    balance = models.PositiveIntegerField(default=5000)
    
