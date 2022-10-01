from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=100,null=True)
    token=models.CharField(max_length=100,null=True)
    is_varified=models.BooleanField(default=False,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
       return self.name