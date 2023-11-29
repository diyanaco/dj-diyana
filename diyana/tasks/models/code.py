from django.db import models

from .mixins import ActivityTrackingModel, UuidPKModel

class Code(ActivityTrackingModel, UuidPKModel):
    CODE_FROM_TYPE_CHOICES = [
        ("CONSTANT", "Constant"),
        ("STATUS", "Status"),  # For task and subtasks
        # ("PROJECT_TYPE", "Project Type"),
    ]
    # Human readable name
    name = models.CharField(max_length=100)
    description = models.TextField()
    from_type = models.CharField(max_length=100,
                                 choices=CODE_FROM_TYPE_CHOICES)
    # Machine readable name
    value_str = models.CharField(max_length=100)
    value_int = models.IntegerField(default=0)
    value_bool = models.BooleanField()

    def __str__(self):
        return f"{self.name} ({self.value_str}, {self.value_int}, {self.value_bool})"