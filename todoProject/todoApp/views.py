from django.shortcuts import render, redirect
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
            return redirect('list.html')
    else:
        form = TaskForm()
    return render(request, 'add.html', {'form':form})

# Read/List all tasks
def read_view(request):
    list_tasks = Tasks.objects.all()
    return render(request, 'list.html', {'list_tasks':list_tasks})

# Update/Edit a task
def update_view(request, task_id):
    update_task = Tasks.objects.get(task_id=task_id)
    form = TaskForm(instance=task_id)
    if request.method == "POST":
        TaskForm(request.POST, instance=update_task)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'update.html', {'form':form})

# Delete a task
def delete_view(request, task_id):
    update_task = Tasks.objects.get(task_id=task_id)
    if request.method == "POST":
        update_task.delete()
        return redirect('list')
    return render(request, 'update.html', {'update-task':update_task})

