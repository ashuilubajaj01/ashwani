from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ItemModel(models.Model):
    name = models.CharField(max_length = 128)
    price = models.IntegerField()
    description = models.TextField(blank=True,null=True)
    cover = models.ImageField(upload_to = 'images/',blank = True,null = True)
    def __str__(self):
        return self.name + " "+ str(self.price)
    
class RestaurentModel(models.Model):
    name = models.CharField(max_length=128)
    place = models.CharField(max_length = 50,blank=True)
    items = models.ManyToManyField(ItemModel,blank=True)

    def __str__(self):
        return self.name

class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.JSONField()
    discount = models.CharField(max_length=128)
    delivery_date = models.DateField(max_length=128,null=True,blank=True)
    def __str__(self):
        return self.user.username
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.total_price = sum(item[1] for item in self.items)
        self.final_price = sum(item[1] for item in self.items) - int(self.discount)

class PromoCodeModel(models.Model):
    promo = models.CharField(max_length=128, blank=True)
    discount = models.CharField(max_length=128)
    description = models.CharField(max_length=128, blank=True)