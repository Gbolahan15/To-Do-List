from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TaskForm

# Create your views here.
# Applying CRUD rule (Create, Read, Update, Delete)

# Create/add a new task
def task_create_view(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create.html', {'form':form})

# Read/List all tasks
def task_read_view(request):
    tasks = Tasks.objects.all()
    return render(request, 'list.html', {'tasks':tasks})

# Update/Edit a task
def task_update_view(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update.html', {'form':form})

# Delete a task
def task_delete_view(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'delete.html', {'task':task})

