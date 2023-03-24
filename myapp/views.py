from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask
# Create your views here.


def index(request):
    title = 'Title Page'
    return render(request, 'index.html', {
        'title': title,
    })

def projects(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'projects.html', {
        'projects': projects,
        'tasks': tasks,
    })



def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        project = request.POST['project']
        Task.objects.create(
            title=title, description=description, project_id=project)
        return redirect('projects')
    projects = Project.objects.all()
    return render(request, 'create_task.html', {
        'form': CreateNewTask,
        'projects': projects
    })
