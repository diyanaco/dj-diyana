from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel
from .task import Task
from .sub_task import Subtask
from .task_list import Tasklist
from .template import Template

class TaskTemplate(ActivityTrackingModel, UuidPKModel):
    tasks = models.ManyToManyField(Task, related_name="tasks")
    subs = models.ManyToManyField(Subtask, related_name="subs")
    lists = models.ManyToManyField(Tasklist, related_name="lists")
    templates = models.ManyToManyField(Template, related_name="template")