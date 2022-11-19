from django.db import models
from .task import Task


class Tag(models.Model):
    title = models.CharField(max_length=30)
    task = models.ManyToManyField(Task)
