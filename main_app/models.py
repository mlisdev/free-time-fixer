from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Activity(models.Model):
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
    finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['timeChoices']
    

