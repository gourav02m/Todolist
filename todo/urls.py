from django.urls import path

from . import views

urlpatterns = [
  
    path('<int:id>', views.remove, name="delete"),
    path('todo',views.home,name='todo'),
]