from django.db import models
from django.utils import timezone

# Create your models here.
class JuZi(models.Model):
    body = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.body

class Book(models.Model):
    STATUS_CHOICES = (
        ('book','Book'),
        ('movie','Movie'),
    )
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='book')
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


