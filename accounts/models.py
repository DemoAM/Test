from django.db import models
from django.contrib.auth.models import User


class Seller(User):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=500)



