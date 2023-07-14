
from django.shortcuts import render, redirect
from .models import Todos




def home(request):
    if request.method == 'POST':
        todolist=request.POST.get('todolist')
        todo = request.POST.get('todo')
        ps=Todos(todo=todo,todolist=todolist,user_id=request.user.id)
        ps.save()
    st=Todos.objects.filter(user_id=request.user.id)
    return render(request, 'home.html',{'st':st})


def remove(request, id):
    item = Todos.objects.get(id=id)
    item.delete()
    # messages.info(request, "item removed !!!")
    return redirect('todo')