from django.db import models
from myauth.models import Profile
from django.dispatch import receiver
import os

class Bill(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    water = models.PositiveIntegerField()
    electric = models.PositiveIntegerField()
    gas = models.PositiveIntegerField()
    charge = models.PositiveIntegerField()
    others = models.PositiveIntegerField()
    details = models.TextField()
    payment_status = models.BooleanField(default=False)
    receipt_photo = models.FileField(upload_to='uploads/receipt_photo/', null=True, blank=True)

class FileHandler:
    """
    Handles file operations, encapsulating the logic for deleting files.
    This makes the code more modular and adheres to the Single Responsibility Principle.
    """
    @staticmethod
    def delete_file(file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)

@receiver(models.signals.post_delete, sender=Bill)
def auto_delete_file_on_delete(sender, instance, kwargs):
    if instance.receipt_photo:
        FileHandler.delete_file(instance.receipt_photo.path)

@receiver(models.signals.pre_save, sender=Bill)
def auto_delete_file_on_change(sender, instance, kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Bill.objects.get(pk=instance.pk).receipt_photo
        if old_file and old_file != instance.receipt_photo:
            FileHandler.delete_file(old_file.path)
    except Bill.DoesNotExist:
        return False