from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Activity(models.Model):
    class TimeChoices(models.IntegerChoices):
        FIFTEEN = 15, _('15 Minutes') 
        HALFHOUR = 30, _('30 Mintues') 
        FOURTYFIVE = 45, _('45 Minutes') 
        HOUR = 60, _('1 Hour') 
        HOURHALF = 90, _('1 Hour 30 Minutes') 
        TWOHOUR = 120, _('2 hours') 
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
    

