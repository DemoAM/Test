from django.db import models
from accounts.models import Seller
class Book(models.Model):
    author = models.ForeignKey(Seller,on_delete=models.SET_DEFAULT,default='Anonymous')
    book_name = models.CharField(max_length=50)
    price = models.IntegerField()
