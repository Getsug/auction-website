from django.shortcuts import render, redirect
from auction.models import ProductRegistration
from .forms import Bid
from . models import BidList
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def currentAuction(request):

    datalist = ProductRegistration.objects.all().filter(application_status='APPROVED')
    topObject = datalist.first()
    highestBid = topObject.minimum_bid

    currentBids = BidList.objects.all()

    for bid in currentBids:
        if bid.bid_amount > highestBid:
            highestBid = bid.bid_amount


    if request.method == 'POST':
        form = Bid(request.POST)

        if form.is_valid():
            buyer = form.save(commit=False)
            buyer.name = request.user
            buyer.save()
            messages.success(request, f'Yor bid has been succesfully submitted!')
            return redirect('manager-currentAuction')
    else:
        form = Bid()

        context = {
            'topObject': topObject,
            'form': form,
            'currentBids' : currentBids,
            'highestBid' :highestBid
        }

    return render(request,'manager/currentAuction.html', context)
