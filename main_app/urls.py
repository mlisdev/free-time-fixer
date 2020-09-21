from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('activities/', views.activities_index, name='index'),
    path('activities/', views.activities_detail, name='detail'),

]