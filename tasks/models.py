from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [('H', 'High'), ('M', 'Medium'), ('L', 'Low')]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # This links the task to a specific user
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title