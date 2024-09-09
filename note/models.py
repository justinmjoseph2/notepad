from django.db import models

# Create your models here.

from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
