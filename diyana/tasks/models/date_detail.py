from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel


class DateDetail(ActivityTrackingModel, UuidPKModel):
    DATE_DETAILS_FROM_TYPE_CHOICES = [
        ("SUB_TASK", "Subtask"),
        ("TASK", "Task"),
        ("TASK_LIST", "Group task"),
        ("MILESTONE", "Milestone Type"),
        ("PHASE", "Phase"),
    ]
    type = models.CharField(max_length=100,
                                 choices=DATE_DETAILS_FROM_TYPE_CHOICES)
    due_date = models.DateTimeField("due date", null=True)
    start_date = models.DateTimeField("start date", null=True)
    reported_date = models.DateTimeField("reported date", null=True)
    actual_start_date = models.DateTimeField("actual start date", null=True)
    actual_end_date = models.DateTimeField("actual end date", null=True)