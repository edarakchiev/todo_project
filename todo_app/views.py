from django.shortcuts import render, redirect

from todo_project.todo_app.forms import CreateTodoForm
from todo_project.todo_app.models import Todo, Person


def index(request):
    context = {
        'todos': Todo.objects.all(),
        'forms': CreateTodoForm(),
    }
    return render(request, 'index.html', context=context)


def create_todo(request):
    form = CreateTodoForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        description = form.cleaned_data['description']

        #owner = Person.objects.filter(name=owner_name).first()

    # if not owner:
    #     owner = Person(name=owner_name)
    #     owner.save()

        todo = Todo(
            title=text,
            description=description,
            # owner=owner
        )
        todo.save()
        return redirect('/')

    context = {
        'todos': Todo.objects.all(),
        'forms': CreateTodoForm(),
    }
    return render(request, 'index.html', context=context)



def change_todo_state(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('/')
