from django.db import models
from myauth.models import Profile

class TicketStatus(models.TextChoices):
    PEND = 'Pending'
    REP = 'Replied'


class ModelManager(models.Manager):

    def update_status(self, id):
        t = Ticket.objects.get(id=id)
        t.status = TicketStatus.REP
        t.save()


class Ticket(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
    status = models.CharField(max_length=10, choices=TicketStatus.choices, default=TicketStatus.PEND)
    reply_description = models.TextField(default=None,blank=True,null=True)
    update = ModelManager().update_status

class Announcement(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)