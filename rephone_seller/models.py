import email
from enum import unique
from django.db import models


class Seller_reg(models.Model):
    username = models.CharField(max_length=100, default=1)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()
    company_name = models.CharField(max_length=30)
    company_adress = models.TextField()
    company_adress_2 = models.TextField()
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.BigIntegerField()
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)


class seller_add_product(models.Model):
    product_name = models.CharField(max_length=300)
    category = models.CharField(max_length=200)
    Available_quantity = models.CharField(max_length=50,default=1)
    product_description = models.CharField(max_length=600)
    percentage_discount = models.CharField(max_length=20)
    MRP = models.BigIntegerField()
    discount_price = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    Seller_id= models.ForeignKey(Seller_reg, on_delete=models.CASCADE)
