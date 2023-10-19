from django.db import models

# Create your models here.
class UserDB(models.Model):
    UserName=models.CharField(max_length=20, null=True, blank=True)
    FullName=models.CharField(max_length=20, null=True, blank=True)
    Email=models.EmailField(max_length=100,null=True, blank=True)
    ContactNumber=models.IntegerField(null=True, blank=True)
    Password=models.CharField(max_length=20, null=True, blank=True)
    Address=models.CharField(max_length=200, null=True, blank=True)
    Image=models.ImageField(upload_to="dp", null=True, blank=True, default="1.png")

class CartDB(models.Model):
    UserName =models.CharField(max_length=20, null=True, blank=True)
    ProName=models.CharField(max_length=20, null=True, blank=True)
    Description=models.CharField(max_length=200, null=True, blank=True)
    Quantity=models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="ProductImages", null=True, blank=True)
    TotalPrice=models.IntegerField(null=True, blank=True)
    Status=models.CharField(max_length=20, null=True, blank=True)

class MessagesDB(models.Model):
    Email=models.EmailField(max_length=100,null=True, blank=True)
    Message=models.CharField(max_length=20,null=True, blank=True)

