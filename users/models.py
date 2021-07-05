from django.db import models

# Create your models here.
user_type=(('1','customer'),
            ('2','seller'),
)
class userdata(models.Model):
    user_type=models.CharField(max_length=8,choices=user_type)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(default="none@example.com")
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    date_time=models.DateTimeField(auto_now_add=True)


