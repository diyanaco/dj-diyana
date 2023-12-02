from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel
from .phase import Phase
from .date_detail import DateDetail
from .tag import Tag


class Tasklist(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phase = models.ForeignKey(Phase,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name="groups")
    date_detail = models.OneToOneField(DateDetail,
                                       on_delete=models.SET_NULL,
                                       null=True)
    tags = models.ManyToManyField(Tag, related_name="tag_grouptasks")