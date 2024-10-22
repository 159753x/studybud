from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host  = models.ForeignKey(User, on_delete = models.CASCADE)

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=300, null=True, blank=True)
    topic = models.ForeignKey(to=Topic, on_delete=models.SET_NULL, null=True, blank=True)

    updated =models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


    def __str__(self) -> str:
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(to = Room, on_delete = models.CASCADE)
    body = models.TextField()
    updated =models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body