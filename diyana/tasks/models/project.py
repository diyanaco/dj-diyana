from django.db import models
from django.contrib.auth.models import Group

from .mixins import ActivityTrackingModel, UuidPKModel


class Project(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    groups = models.ManyToManyField(Group, related_name="projects")
