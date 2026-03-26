from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=50, default="Beginner")
    
    # Extra fields
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)

    # Store coins in Copper (IMPORTANT)
    copper_coin = models.IntegerField(default=0)
    bronze_coin = models.IntegerField(default=0)
    silver_coin = models.IntegerField(default=0)
    gold_coin = models.IntegerField(default=0)
    platinum_coin = models.IntegerField(default=0)
    titanium_coin = models.IntegerField(default=0)
    mithril_coin = models.IntegerField(default=0)
    dragon_coin = models.IntegerField(default=0)


    
    
    

    def __str__(self):
        return self.user.username