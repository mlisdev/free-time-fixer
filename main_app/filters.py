from django.contrib.auth.models import User
import django_filters
from .models import Activity
from django import forms 

class ActivityFilter(django_filters.FilterSet):
    class Meta:
        model = Activity
        fields = {
            'category': ['exact'],
            'timeChoices': ['lte']
        }

    



        