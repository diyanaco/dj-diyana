from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel


class Tag(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)