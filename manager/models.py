from django.db import models
from django.contrib.auth.models import User


class BidList(models.Model):

    STATUS_CHOICES = [
    ("TOPBIDDER", 'Top bidder'),
    ("CONTENDER", 'Contender'),
    ]

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices = STATUS_CHOICES, default="CONTENDER")


    def __str__(self):
        return f'{self.name.username}\'s Bid'
