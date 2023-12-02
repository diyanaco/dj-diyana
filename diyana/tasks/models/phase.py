from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel
from .priority import Priority
from .date_detail import DateDetail


class Phase(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.OneToOneField(Priority,
                                    on_delete=models.SET_NULL,
                                    null=True)
    date_detail = models.OneToOneField(DateDetail,
                                       on_delete=models.SET_NULL,
                                       null=True)

    def __str__(self):
        return f"{self.name} (Priority : {self.priority})"
