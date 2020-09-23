from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Activity
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .filters import ActivityFilter
# Create your views here.

class ActivityCreate(LoginRequiredMixin, CreateView):
    model = Activity
    fields = ['timeChoices', 'name', 'description', 'category']
    success_url = '/activities/'
    def form_valid(self,form):
      form.instance.user = self.request.user
      return super().form_valid(form)



class ActivityDelete(LoginRequiredMixin, DeleteView):
    model = Activity
    success_url = '/activities/'


def home(request):
  return render(request, 'home.html')

@login_required
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
      return redirect('detail')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def search(request):
    a = ActivityFilter(request.GET, queryset=Activity.objects.filter(user=request.user).order_by('?'))
    b = a.qs[:1]
    # entry_list = list(Activity.objects.filter(user=request.user))
    print('SHIT', b)
    return render(request, 'search.html', {'filter': a, 'anything': b})
