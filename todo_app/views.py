from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Todo

# Create your views here.

def home(request):
    return HttpResponse("Hello Jade! start small and win big! I'm proud of you!")

class todo_index(ListView):
    template_name = 'index.html'
    paginate_by = 5
    context_object_name = 'todo_list'

    def get_queryset(self):
        """ Return all the latest Todo's """
        return Todo.objects.order_by('-created_at')

def todo_add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)

    return redirect('todo:todo_index')

def todo_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()

    return redirect('todo:todo_index')

def todo_update(request, id):
    todo = get_object_or_404(Todo, pk=id)
    status = request.POST.get('isCompleted', False)

    if status == 'on':
        status = True
    
    todo.isCompleted = status

    todo.save()

    return redirect('todo:todo_index')





