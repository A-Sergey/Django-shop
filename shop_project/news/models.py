from django.db import models
from django.utils import timezone
from accounts.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    publish = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title