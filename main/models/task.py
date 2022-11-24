from django.db import models
from .user import User


class Task(models.Model):
    class States(models.TextChoices):
        NEW_TASK = "new task"
        IN_DEVELOPMENT = "in development"
        IN_QA = "in qa"
        IN_CODE_REVIEW = "in code review"
        READY_FOR_RELEASE = "ready for release"
        RELEASED = "released"
        ARCHIVED = "archived"

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_created = models.DateField()
    date_modified = models.DateField()
    date_completed = models.DateField()
    state = models.CharField(
        max_length=20, default=States.NEW_TASK, choices=States.choices
    )
    task_creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creators"
    )
    task_performer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="performers"
    )
