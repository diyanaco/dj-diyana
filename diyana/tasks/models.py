import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    Group,
    User,
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)


class UuidPKModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, UuidPKModel, PermissionsMixin):
    email = models.EmailField(unique=True)
    # username = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    # Email is used as the authentication field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.email


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
    due_date = models.DateTimeField("due date")
    start_date = models.DateTimeField("start date")
    reported_date = models.DateTimeField("reported date")
    actual_start_date = models.DateTimeField("actual start date")
    actual_end_date = models.DateTimeField("actual end date")


class Code(ActivityTrackingModel, UuidPKModel):
    CODE_FROM_TYPE_CHOICES = [
        ("CONSTANT", "Constant"),
        ("STATUS", "Status"),  # For task and subtasks
        ("PROJECT_TYPE", "Project Type"),
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


class Project(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)


class ProjectGroupLink(ActivityTrackingModel, UuidPKModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False)


class Phase(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.OneToOneField(Priority,
                                    on_delete=models.SET_NULL,
                                    null=True)
    date_detail = models.ForeignKey(DateDetail,
                                    on_delete=models.SET_NULL,
                                    null=True)

    def __str__(self):
        return f"{self.name} (Priority : {self.priority})"


class ProjectPhaseTemplateLink(ActivityTrackingModel, UuidPKModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, null=False)


class Milestone(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    phase = models.ForeignKey(Phase, on_delete=models.SET_NULL, null=True)
    date_detail = models.ForeignKey(DateDetail,
                                    on_delete=models.SET_NULL,
                                    null=True)


class Tag(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)


class GroupTask(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phase = models.ForeignKey(Phase, on_delete=models.SET_NULL, null=True)
    date_detail = models.ForeignKey(DateDetail,
                                    on_delete=models.SET_NULL,
                                    null=True)
    tags = models.ManyToManyField(Tag, related_name="tag_grouptasks")


class Task(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="task_assigned_to")
    reported_by = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="task_reported_by")
    priority = models.OneToOneField(Priority,
                                    on_delete=models.SET_NULL,
                                    null=True)
    status = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(GroupTask, on_delete=models.SET_NULL, null=True)
    date_detail = models.ForeignKey(DateDetail,
                                    on_delete=models.SET_NULL,
                                    null=True)
    tags = models.ManyToManyField(Tag, related_name="tag_tasks")


class Subtask(ActivityTrackingModel, UuidPKModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ForeignKey(Task,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name="subs")
    reported_by = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="subtask_reported_by")
    assigned_to = models.ForeignKey(User,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    related_name="subtask_assigned_to")
    priority = models.OneToOneField(Priority,
                                    on_delete=models.SET_NULL,
                                    null=True)
    status = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)
    date_detail = models.ForeignKey(DateDetail,
                                    on_delete=models.SET_NULL,
                                    null=True)
    tags = models.ManyToManyField(Tag, related_name="tag_subtasks")
