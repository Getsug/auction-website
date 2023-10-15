from django.shortcuts import render, redirect
from .forms import RequestItemApproval
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request,'auction/home.html')


@login_required
def registerProduct(request):
    if request.method == 'POST':
        form = RequestItemApproval(request.POST)

        if form.is_valid():
            seller = form.save(commit=False)
            seller.seller_name = request.user
            seller.save()
            messages.success(request, f'Yor application has been succesfully submitted!')
            return redirect('auction-registerProduct')
    else:
        form = RequestItemApproval()

    return render(request,'auction/registerProduct.html', {'form': form})
