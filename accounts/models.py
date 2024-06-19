from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Seller(AbstractBaseUser):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    user_type = models.CharField(max_length=15,choices={'seller':'Seller'},default="Seller")

    def Is_seller(self):
        return bool(self.user_type=='seller')



