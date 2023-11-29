from django.db import models
from django.contrib.auth.models import Group

from .mixins import ActivityTrackingModel, UuidPKModel
from .phase import Phase
from .project_template_phase import ProjectTemplatePhase


class Project(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=100)
    teams = models.ManyToManyField(Group, related_name="projects")
    template = models.ForeignKey(ProjectTemplatePhase,
                                 related_name='projects',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 to_field="template")
    phases = models.ManyToManyField(Phase,
                                    related_name="projects",
                                    through="ProjectTemplatePhase")
