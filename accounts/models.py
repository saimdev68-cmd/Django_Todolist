from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email 
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="profile")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="profile/",default="default.png")

    def __str__(self):
        return self.name
    
    