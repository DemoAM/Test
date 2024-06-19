from django.db import models
from django.contrib.auth.models import  AbstractBaseUser


class Seller (AbstractBaseUser):
    USER_ROLES = {
        'seller' : 'Seller'
    }
    name = models.CharField(("Name"),max_length=254)
    email=models.EmailField(("Email"), max_length=254)
    user_type = models.CharField(max_length=254,choices=USER_ROLES,default='Seller')
    password = models.CharField(("Password"),max_length=254)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','email','password']


    def __str__(self):
        return self.name








