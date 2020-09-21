from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('activities/', views.activities_index, name='index'),
    path('activities/create/', views.ActivityCreate.as_view(), name='activities_create'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activities_delete'),

]