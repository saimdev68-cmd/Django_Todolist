from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Task(models.Model):
    STATUS_CHOICE = [
        ("pending","Pending"),
        ("processing","Processing"),
        ("completed","Completed"),
        ("cancel","Cancel"),
        ("failed","Failed")
    ]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="tasks")
    title = models.CharField(max_length=300)
    status = models.CharField(max_length=100,choices=STATUS_CHOICE,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]