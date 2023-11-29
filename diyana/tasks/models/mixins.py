import uuid
from django.db import models

from .user import User


class UuidPKModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class ActivityTrackingModel(models.Model):

    ACTIVITY_TRACKING_FIELDS = [
        'created_at',
        'created_by',
        'updated_at',
        'updated_by',
    ]

    class Meta:
        abstract = True

    created_by = models.ForeignKey(User,
                                   on_delete=models.SET_NULL,
                                   related_name='%(class)s_created',
                                   null=True)
    updated_by = models.ForeignKey(User,
                                   on_delete=models.SET_NULL,
                                   related_name='%(class)s_updated',
                                   null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)