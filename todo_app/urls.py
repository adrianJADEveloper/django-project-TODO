from django.urls import path, include
from . import views

app_name = 'todo'
urlpatterns = [
    path('home', views.home, name='home'), # You can do it Jade!
    path('', views.todo_index.as_view(), name='todo_index'),
    path('add', views.todo_add, name='todo_add'),
    path('delete/<int:id>', views.todo_delete, name='todo_delete'),
    path('update/<int:id>', views.todo_update, name='todo_update'),
    
]