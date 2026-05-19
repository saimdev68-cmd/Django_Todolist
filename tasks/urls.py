from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("Task/Create/",views.TaskCreateView.as_view(),name="task_create"),
    path("Task/<int:pk>/Update/",views.TaskUpdateView.as_view(),name="task_update"),
    path("delete_task/<int:pk>/",views.TaskDeleteView.as_view(),name="task_delete"),
    path("status/<int:pk>/",views.ProcessingStatus.as_view(),name="status")
]
