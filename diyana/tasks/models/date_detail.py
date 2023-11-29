from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel


class DateDetail(ActivityTrackingModel, UuidPKModel):
    DATE_DETAILS_FROM_TYPE_CHOICES = [
        ("SUB_TASK", "Subtask"),
        ("TASK", "Task"),
        ("GROUP_TASK", "Group task"),
        ("MILESTONE", "Milestone Type"),
        ("PHASE", "Phase"),
    ]
    from_type = models.CharField(max_length=100,
                                 choices=DATE_DETAILS_FROM_TYPE_CHOICES)
    # The first optional argument to a Field is the human-readable name.
    # If this isn’t given, Django will use the machine-readable name.
    # In this example, we’ve only defined a human-readable name for DateDetail.due_date.
    # For all other fields in this model, the field’s machine-readable name will suffice as its human-readable name.
    due_date = models.DateTimeField("due date", null=True)
    start_date = models.DateTimeField("start date", null=True)
    reported_date = models.DateTimeField("reported date", null=True)
    actual_start_date = models.DateTimeField("actual start date", null=True)
    actual_end_date = models.DateTimeField("actual end date", null=True)