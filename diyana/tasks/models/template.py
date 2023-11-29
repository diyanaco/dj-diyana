from django.db import models
from .mixins import ActivityTrackingModel, UuidPKModel
from .phase import Phase

class Template(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phases = models.ManyToManyField(Phase,
                                    related_name="template",
                                    through="ProjectTemplatePhase")