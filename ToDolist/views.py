from django.shortcuts import render, redirect
from .models import Todo
from django.http import Http404
from django.http import HttpResponse
from datetime import datetime, date
from django.utils.timezone import get_current_timezone
#from .forms import TodoListForm
from django.contrib import auth

# Create your views here.


def index(request):
    username = auth.get_user(request)
    creator = username.id
    todos = Todo.objects.filter(finished=False, creator_id=username.id)
    finishedtodos = Todo.objects.filter(finished=True)
    context = {
        'creator_id': creator,
        'username': username,
        'todos': todos,
        'finishedtodos': finishedtodos,
    }
    return render(request, 'todolist/index.html', context)


def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {

        'todo': todo,
    }
    return render(request, 'todolist/details.html', context)


def add(request):
    if(request.method == 'POST'):
        creator = (auth.get_user(request)).id
        title = request.POST['title']
        text = request.POST['text']
        priority = request.POST['priority']
        deadlinea = request.POST['deadlinea']
        todo = Todo(title=title, text=text, priority=priority, deadline=deadlinea, creator_id=creator)
        todo.save()

        return redirect('/')
    else:
        return render(request, 'todolist/add.html')


def edit(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo,
    }

    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        text = request.POST['text']
        priority = request.POST['priority']
        todo = Todo.objects.filter(id=id).update(text=text, priority=priority)
        return redirect('/')
    else:
        return render(request, 'todolist/edit.html', context)


def delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
    return redirect('/')


def finished(request, id):
    try:
        username = auth.get_user(request)
        todo = Todo.objects.get(id=id)

    except Exception:
        raise Http404
    if todo and username.id == todo.creator_id:
        if todo.finished == False:
            todo = Todo.objects.filter(id=id, creator_id=username.id).update(finished=True, finished_at=datetime.now())
        else:
            todo = Todo.objects.filter(id=id, creator_id=username.id).update(finished=False)
    return redirect('/')