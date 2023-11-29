from django.db import models
from .mixins import ActivityTrackingModel, UuidPKModel
from .template import Template
from .phase import Phase
from .project import Project

class ProjectTemplatePhase(ActivityTrackingModel, UuidPKModel):

    class Meta:
        db_table = 'tasks_project_template_phases'

    template = models.ForeignKey(Template,
                                 on_delete=models.SET_NULL,
                                 null=True)
    phase = models.ForeignKey(Phase, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project,
                                on_delete=models.SET_NULL,
                                null=True,
                                unique=True)