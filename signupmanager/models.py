from django.db import models

# Create your models here.
class userdata(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=256)
    utype = models.CharField(max_length=32)
