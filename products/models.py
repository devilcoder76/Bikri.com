from django.db import models

# Create your models here.

class product(models.Model):
    seller_id=models.IntegerField(default=-1)
    title=models.CharField(max_length=40)
    desc=models.TextField()
    price=models.FloatField()
    date_time=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='product/images')

class orders(models.Model):
    customer_id=models.IntegerField(default=-1)
    product_id=models.IntegerField(default=-1)
    qty=models.IntegerField(default=-1)
    date_time=models.DateTimeField(auto_now_add=True)
    