from django.db import models
from django.contrib.auth.models import User


class UserWallet(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default = 50000)


    def __str__(self):
        return f'{self.user.username}\'s Wallet'
