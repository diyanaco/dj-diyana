from django.db import models
from .mixins import ActivityTrackingModel, UuidPKModel
from .phase import Phase
from .task import Task


class Template(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
