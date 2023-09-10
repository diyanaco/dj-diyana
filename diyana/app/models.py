from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DateDetail(models.Model):
    # The first optional argument to a Field is the human-readable name. 
    # If this isn’t given, Django will use the machine-readable name. 
    # In this example, we’ve only defined a human-readable name for DateDetail.due_date. 
    # For all other fields in this model, the field’s machine-readable name will suffice as its human-readable name.
    due_date = models.DateTimeField('due date')
    start_date = models.DateTimeField('start date')
    reported_date = models.DateTimeField('reported date')

class Code(models.Model):
    # Human readable name
    name = models.CharField(max_length=200)
    # Machine readable name
    value = models.CharField(max_length=200)
    # Acceptted values
    # 1. Priority
    # 2. Status
    # 3. User Type
    type = models.CharField(max_length=200)

class Milestone(models.Model):
    date_details = models.ForeignKey(DateDetail, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    phase = models.CharField(max_length=200)

class GroupTask(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()   
    milestone = models.ForeignKey(Milestone, on_delete=models.SET_NULL, null=True)

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_details = models.ForeignKey(DateDetail, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Code, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(GroupTask, on_delete=models.SET_NULL, null=True)
