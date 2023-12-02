from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel
from .phase import Phase
from .date_detail import DateDetail


class Milestone(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    date_detail = models.OneToOneField(DateDetail,
                                       on_delete=models.SET_NULL,
                                       null=True)
