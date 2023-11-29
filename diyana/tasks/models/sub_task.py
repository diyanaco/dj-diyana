from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel
from .task import Task
from .user import User
from .priority import Priority
from .code import Code
from .date_detail import DateDetail
from .tag import Tag


class Subtask(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ForeignKey(Task,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name="subs")
    reported_by = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="subtask_reported_by")
    assigned_to = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="subtask_assigned_to")
    priority = models.OneToOneField(Priority,
                                    on_delete=models.SET_NULL,
                                    null=True)
    status = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)
    date_detail = models.OneToOneField(DateDetail,
                                       on_delete=models.SET_NULL,
                                       null=True)
    tags = models.ManyToManyField(Tag, related_name="tag_subtasks")
