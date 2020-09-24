from django.contrib.auth.models import User
import django_filters
from .models import Activity
from django import forms
from django.utils.translation import gettext_lazy as _


class ActivityFilter(django_filters.FilterSet):
    TIME_CHOICES = (
        (15, _('15 Minutes')), 
        (30, _('30 Mintues')), 
        (45, _('45 Minutes')),
        (60, _('1 Hour')), 
        (90, _('1 Hour 30 Minutes')), 
        (120, _('2 hours')), 
    )
    timeChoices = django_filters.ChoiceFilter(choices=TIME_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-sm'}), lookup_expr='lte')
    class Meta:
        model = Activity
        fields = [ 'category', 'timeChoices' ]
        
    

    



        