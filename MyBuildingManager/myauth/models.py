from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    house_number = models.PositiveIntegerField()
    floor_number = models.PositiveIntegerField()
    is_admin = models.BooleanField(default=False)

