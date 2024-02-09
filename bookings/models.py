# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from room.models import Room
from django.contrib.auth.models import User


# Create your models here.
class Guest(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone=models.IntegerField()
    address = models.CharField(blank=True, max_length=150)
    country = models.CharField(blank=True, max_length=20)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    stay=models.IntegerField(default=0)

    def __str__(self):
        return self.room.name

    @property
    def totalamount(self):
        return self.stay * self.room.price
