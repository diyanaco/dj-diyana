from django.db import models
from .mixins import ActivityTrackingModel, UuidPKModel
from .user import User
from .priority import Priority
from .code import Code
from .task_list import Tasklist
from .date_detail import DateDetail
from .tag import Tag

class Task(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="task_assigned_to")
    reported_by = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="task_reported_by")
    priority = models.OneToOneField(Priority,
                                    on_delete=models.SET_NULL,
                                    null=True)
    status = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)
    list = models.ForeignKey(Tasklist,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name="tasks")
    date_detail = models.OneToOneField(DateDetail,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       related_name="task")
    tags = models.ManyToManyField(Tag, related_name="tag_tasks")