from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from .utils import getFlipkartItems
from django.contrib import messages
# Create your models here.

class ItmePrice(models.Model):
    url = models.URLField(max_length=500)
    item_title = models.CharField(max_length=255, blank=True, null=True)
    current_price = models.IntegerField(blank=True, null=True)
    old_price = models.IntegerField(blank=True, null=True, default=0)
    price_difference = models.IntegerField(blank=True, null=True, default=0)
    image_link = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    class Meta:
        ordering = ('price_difference','-created',)
        
    def __str__(self) -> str:
        return self.item_title
    
    def save(self, *args, **kwargs):
        try:
            title,price,image_url = getFlipkartItems(self.url)
            old_price = self.current_price
            
            # this code will be exicuted if record updated 
            if self.current_price:
                # if price are changed then 
                if price != old_price:
                    
                    price_diff = price-old_price
                    self.price_difference = round(price_diff,2)
                    self.old_price = old_price
                    self.current_price = price
                else:
                    self.old_price = 0
                    self.price_difference = 0
            self.item_title = title
            self.current_price = price
            self.image_link = image_url
                
            super().save(*args, **kwargs)
        except Exception as e:
            return e