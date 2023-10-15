from django.shortcuts import render
from auction.models import ProductRegistration
from django.contrib.auth.decorators import login_required


@login_required
def approvedList(request):

    dblist = ProductRegistration.objects.all().filter(application_status='APPROVED')

    return render(request,'company/approvedList.html', {'dblist': dblist})
