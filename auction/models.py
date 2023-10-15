from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ProductRegistration(models.Model):

    STATUS_CHOICES = [
    ("APPROVED", 'Approved'),
    ("REJECTED", 'Rejected'),
    ("WAITING", 'Waiting'),
    ]

    AUCTION_CHOICES = [
    ("ACTIVE", 'Active'),
    ("EXPIRED", 'Expired'),
    ("WAITING", 'Waiting'),
    ]

    seller_name = models.ForeignKey(User, on_delete=models.CASCADE)
    seller_email = models.EmailField()
    product = models.CharField(max_length=100)
    description = models.TextField()
    minimum_bid = models.PositiveIntegerField()
    auction_timespan = models.PositiveIntegerField()                 #in minutes
    date_registered =  models.DateTimeField(default=timezone.now)
    auction_start = models.DateTimeField(default=timezone.now)
    auction_end = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    application_status = models.CharField(max_length=10, choices = STATUS_CHOICES, default="WAITING")
    auction_status = models.CharField(max_length=10, choices = AUCTION_CHOICES, default="WAITING")

    def __str__(self):
        return f'{self.seller_name.username}\'s Application'
