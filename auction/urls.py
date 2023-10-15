from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='auction-home'),
    path('registerProduct/', views.registerProduct, name='auction-registerProduct'),
]
