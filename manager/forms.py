from django import forms
from .models import BidList


class Bid(forms.ModelForm):

    class Meta:
       model = BidList
       #fields = '__all__'
       exclude = ['name', 'status']
