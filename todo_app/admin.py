from django.contrib import admin
from todo_project.todo_app.models import Todo, Person, Category

admin.site.register(Todo)
admin.site.register(Person)
admin.site.register(Category)
