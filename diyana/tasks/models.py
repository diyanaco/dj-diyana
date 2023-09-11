from django.db import models
from django.contrib.auth.models import User, Group


class DateDetail(models.Model):
    DATE_DETAILS_FROM_TYPE_CHOICES = [
        ('SUB_TASK', 'Subtask'),
        ('TASK', 'Task'),
        ('GROUP_TASK', 'Group task'),
        ('MILESTONE', 'Milestone Type'),
        ('PHASE', 'Phase'),
    ]
    from_type = models.CharField(max_length=100,
                                 choices=DATE_DETAILS_FROM_TYPE_CHOICES)
    # The first optional argument to a Field is the human-readable name.
    # If this isn’t given, Django will use the machine-readable name.
    # In this example, we’ve only defined a human-readable name for DateDetail.due_date.
    # For all other fields in this model, the field’s machine-readable name will suffice as its human-readable name.
    due_date = models.DateTimeField('due date')
    start_date = models.DateTimeField('start date')
    reported_date = models.DateTimeField('reported date')
    actual_start_date = models.DateTimeField('actual start date')
    actual_end_date = models.DateTimeField('actual end date')


class Code(models.Model):
    CODE_FROM_TYPE_CHOICES = [
        ('CONSTANT', 'Constant'),
        ('STATUS', 'Status'),
        ('PROJECT_TYPE', 'Project Type'),
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
        return f'{self.name} ({self.value_str}; {self.value_int}; {self.value_bool})'


class Priority(models.Model):
    PRIORITY_VALUE_STR_CHOICES = [
        ('LOW', 'Low'),
        ('LOW_MEDIUM', 'Low Medium'),
        ('MEDIUM', 'Medium'),
        ('MEDIUM_HIGH', 'Medium High'),
        ('HIGH', 'High'),
    ]
    urgency = models.IntegerField(default=0)
    gravity = models.IntegerField(default=0)
    criticality = models.IntegerField(default=0)
    value_int = models.IntegerField(default=0)
    # From value_int (in percentage), will divide by 5 segment
    # LOW, LOW_MEDIUM, MEDIUM, MEDIUM_HIGH, HIGH
    value_str = models.CharField(max_length=100,
                                 choices=PRIORITY_VALUE_STR_CHOICES)


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)


class ProjectGroupLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False)


class Phase(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.ForeignKey(Priority,
                                 on_delete=models.SET_NULL,
                                 null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    date_details = models.ForeignKey(DateDetail,
                                     on_delete=models.SET_NULL,
                                     null=True)


class Milestone(models.Model):
    date_details = models.ForeignKey(DateDetail,
                                     on_delete=models.SET_NULL,
                                     null=True)
    name = models.CharField(max_length=100)
    phase = models.ForeignKey(Phase, on_delete=models.SET_NULL, null=True)


class GroupTask(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phase = models.ForeignKey(Phase, on_delete=models.SET_NULL, null=True)
    date_details = models.ForeignKey(DateDetail,
                                     on_delete=models.SET_NULL,
                                     null=True)


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name='task_assigned_to')
    reported_by = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name='task_reported_by')
    priority = models.ForeignKey(Priority,
                                 on_delete=models.SET_NULL,
                                 null=True)
    status = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(GroupTask, on_delete=models.SET_NULL, null=True)
    date_details = models.ForeignKey(DateDetail,
                                     on_delete=models.SET_NULL,
                                     null=True)


class Subtask(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    reported_by = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name='subtask_reported_by')
    assigned_to = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name='subtask_assigned_to')
    priority = models.ForeignKey(Priority,
                                 on_delete=models.SET_NULL,
                                 null=True)
    status = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)
    date_details = models.ForeignKey(DateDetail,
                                     on_delete=models.SET_NULL,
                                     null=True)
