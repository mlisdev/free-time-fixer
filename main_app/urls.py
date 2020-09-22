from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('activities/', views.activities_detail, name='detail'),
    path('activities/create/', views.ActivityCreate.as_view(), name='activities_create'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activities_delete'),
    # using regex with path needs re_path
    re_path(r'^search/$', views.search, name='search'),
]