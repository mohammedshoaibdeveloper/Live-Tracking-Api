from django.db import models
from rest_framework import serializers

Device = (

        ('ios','ios'),
        ('android','android'),
         ('web','web'),

    )

class Signup(models.Model):


    id = models.AutoField(primary_key=True)
    Full_Name=models.TextField(default="")
    Email=models.TextField(default="")
    Username=models.TextField(default="")
    Password=models.TextField(default="")
    Image=models.ImageField(upload_to='Signup/',default="Health_Professional/dummy.jpg")
    Sender_ID = models.TextField(default="")
    Device_type = models.CharField(max_length=100,choices=Device,default="android")
    latitude = models.CharField(max_length=100,default="")
    longitude = models.CharField(max_length=100,default="")
   




    def __str__(self):
        return self.Full_Name


class SerSignup(serializers.ModelSerializer):
    class Meta:
        model = Signup
        
        fields = '__all__'