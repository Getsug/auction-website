from django.shortcuts import render
from . models import UserWallet
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def wallet(request):

    userwallet = UserWallet.objects.all()

    loggedinUser = request.user

    context = {
        'title': 'Wallet',
        'userwallet': userwallet,
        'loggedinUser' : loggedinUser
        }

    return render(request,'wallet/wallet.html', context)
