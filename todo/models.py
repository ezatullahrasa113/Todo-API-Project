from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user= models.ForeignKey(User,on_delete = models.CASCADE,null = True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    ROLE_CHOICES=(
        ('admin','Admin'),
        ('user','User')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='user')
