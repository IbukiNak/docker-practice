from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
    path("", mytodo.index, name="index"),
    path("add/", mytodo.add, name="add"),
    path("<str:task_id>/edit/", mytodo.edit, name="edit"),
    path("update_task_complete/", mytodo.update_task_complete, name="update_task_complete"),
    path("delete/", mytodo.delete, name="delete"),
    
]
