from django.shortcuts import render
from home.models import Task



# Create your views here.
def home(request):
  tasks = Task.objects.filter(is_completed = False)
  completed_tasks = Task.objects.filter(is_completed = True)
  context = {
        'tasks':tasks,
        'completed_tasks': completed_tasks
  }

  
  return render(request, 'home.html', context)

