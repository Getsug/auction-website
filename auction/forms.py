from django import forms
from .models import ProductRegistration


class RequestItemApproval(forms.ModelForm):

    class Meta:
       model = ProductRegistration
       #fields = '__all__'
       exclude = ['seller_name','date_registered','auction_start','auction_end','application_status', 'auction_status']
