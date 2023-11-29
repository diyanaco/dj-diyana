from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel

class Priority(ActivityTrackingModel, UuidPKModel):
    PRIORITY_VALUE_STR_CHOICES = [
        ("LOW", "Low"),
        ("LOW_MEDIUM", "Low Medium"),
        ("MEDIUM", "Medium"),
        ("MEDIUM_HIGH", "Medium High"),
        ("HIGH", "High"),
    ]
    urgency = models.IntegerField(default=0)
    gravity = models.IntegerField(default=0)
    criticality = models.IntegerField(default=0)
    value_int = models.IntegerField(default=0)
    # From value_int (in percentage), will divide by 5 segment
    # LOW, LOW_MEDIUM, MEDIUM, MEDIUM_HIGH, HIGH
    value_str = models.CharField(max_length=100,
                                 choices=PRIORITY_VALUE_STR_CHOICES)

    def __str__(self):
        return f"{self.value_str}"