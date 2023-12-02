from django.db import models
from .mixins import ActivityTrackingModel, UuidPKModel
from .task import Task
from .sub_task import Subtask
from .task_list import Tasklist
from .phase import Phase

class Template(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tasks = models.ManyToManyField(Task, related_name="tasks")
    subs = models.ManyToManyField(Subtask, related_name="subs")
    lists = models.ManyToManyField(Tasklist, related_name="lists")
    phases = models.ManyToManyField(Phase, related_name="phases")
