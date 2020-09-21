from django.db import models
from django.contrib.auth.models import User
# what is this? 
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Activities(models.Model):
    class TimeChoices(models.IntegerChoices):
        FIFTEEN = 15 
        HALFHOUR = 30
        FOURTYFIVE = 45
        HOUR = 60
        HOURHALF = 90
        TWOHOUR = 120
    timeChoices = models.IntegerField(choices=TimeChoices.choices)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    class Category(models.TextChoices):
        WATCH = 'Watch'
        READ = 'Read'
        FITNESS = 'Fitness'
        PLAY = 'Play'
    # added max length 
    category = models.CharField(max_length=100, choices=Category.choices)
    finished = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

