from django.db import models
from datetime import datetime

# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    description=models.TextField()
    company=models.CharField(max_length=100, blank=False)
    email=models.CharField(max_length=100, blank=False)
    created_at=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title