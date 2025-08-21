from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_read_view, name="task_list"),
    path('create/', views.task_create_view, name="task_create"),
    path('update/<int:task_id>/', views.task_update_view, name="task_update"),
    path('delete/<int:task_id>/', views.task_delete_view, name="task_delete"),
]