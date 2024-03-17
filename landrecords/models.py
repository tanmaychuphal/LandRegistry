from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class loginData(models.Model):
    username = models.CharField(max_length=50, default="", blank=True)
    email = models.CharField(max_length=100, default="", blank=True)
    password = models.CharField(max_length=1000,default="", blank=True)


class newEntry(models.Model):
    name=models.CharField(max_length=50,default="",blank=False)
    # fname=models.CharField(max_length=50,default="",blank=False)
    state=models.CharField(max_length=50,default="",blank=False)
    # district=models.CharField(max_length=50,default="",blank=False)
    city=models.CharField(max_length=50,default="",blank=False)
    pincode=models.CharField(max_length=10)
    # code=models.ImageField(blank=True,upload_to='code')
    image = models.ImageField(upload_to='images/',default='default_image.jpg')
    # def __str__(self) -> str:
    #     return self.name,self.fname,self.state,self.district,self.city,self.pincode 
