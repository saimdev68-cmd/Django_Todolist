from django.views import generic , View
from .forms import  TaskForm
from .models import  Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect , get_object_or_404
from django.db.models import Count , Q

# Create your views here.

class HomeView(LoginRequiredMixin,generic.ListView):
    template_name = "home.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)[:10]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(user=self.request.user)
        context["stats"] = tasks.aggregate(
            total_tasks = Count("id"),
            complete_tasks = Count("id",filter=Q(status="completed")),
            pending_tasks = Count("id",filter=Q(status="pending")),
            processing_tasks = Count("id",filter=Q(status="processing")),
            failed_tasks = Count("id",filter=Q(status="failed")),
            cancel_tasks = Count("id",filter=Q(status="cancel")),
        )
        return context
    
class TaskCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "task_create.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class TaskUpdateView(LoginRequiredMixin,generic.UpdateView):
    template_name = "task_update.html"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:home")

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class TaskDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home")

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
        
class ProcessingStatus(LoginRequiredMixin,View):
    def post(self,request,pk):
        task = get_object_or_404(Task,user=request.user,pk=pk)
        if task.status == "pending":
            task.status = "processing"
            task.save()
            return redirect ("todo:home")
        else:
            task.status = "completed"
            task.save()
            return redirect ("todo:home")
        