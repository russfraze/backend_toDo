from django.db import models

class Todo(models.Model):
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
