from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    note = models.CharField(max_length=200, default="none")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

