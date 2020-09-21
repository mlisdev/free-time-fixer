from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Activity
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class ActivityCreate(LoginRequiredMixin, CreateView):
    model = Activity

class ActivityDelete(LoginRequiredMixin, DeleteView):
    model = Activity

def home(request):
  return render(request, 'home.html')

def activities_index(request):
    return render(request, 'activities/index.html')

@login_required
def activities_detail(request):
    activities = Activity.objects.filter(user=request.user)
    return render(request, 'activities/detail.html', {
        'activities': activities
    })

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)