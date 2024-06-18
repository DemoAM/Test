from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import SellerSerializer,Seller
# Create your views here.
class DetailSeller(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    http_method_names = ['post']
    