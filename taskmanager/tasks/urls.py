from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index")
]

urlpatterns += [
    path('tasks/createTask/', views.createTask , name="createTask")
]