from django.db import models
from django.db import models
from django.conf import settings
from profiles.models import profile
from datetime import *
# Create your models here.
#Time Table for a Day
Priority_Options = [('1','Normal'),('2','Preferred'), ('3','Important'), ('4','Indespensable')]
Event_Timings = [('B','Fixed Timing'),('C',('Variable Timing'))]
Event_Type = [('A','Official Classes'), ('B','Study Acads'), ('C','Extra Study'), ('D','ExtraCurriculars'),('E','Misc.')]
Duration_choices = [('1','Half Hour'),('2','One Hour'),('3','One and Half Hour'),('4','Two Hour'),('5',"Two and Half Hour"),('6','Three Hour'),('8','Four Hour'), ('10','Five Hours'),('12','Six Hours')]

## A model named DailySched
# @details It contains the fields UserProfile which has a foreignkey to the profile model,
# a datefileld called Active_Day, and a name which is a characterfield.
class DailySched(models.Model):
	UserProfile = models.ForeignKey(profile, on_delete=models.CASCADE)
	Active_day = models.DateField()
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

defaultDeadLine = date.today()+timedelta(days=3)

## A model named Event
# @details The most elementary model of the project.It contains all the fields that specifies all the details 
# of an event. CreatorType corresponds to what type of event an instructor is creating i.e, assignments,
# classes, exams etc. Creatorid correspond to the id of the respective type of event(model).
# Completed is a booleanfield which stores whether the event is completed or not.

class Event(models.Model):
	"""docstring for Event."""
	UserProfile = models.ForeignKey(profile, on_delete=models.CASCADE)
	CreatorType = models.CharField(max_length=1,default='0')
	CreatorId = models.CharField(max_length=100,null=True)
	name = models.CharField(max_length=50)
	Description = models.CharField(max_length=300,blank=True)
	Venue = models.CharField(max_length=100,blank=True)
	StartTime = models.TimeField(null=True,)#removed Blank notequaltoTrue for some case
	StartDate = models.DateField(null=True,default=date.today)
	Duration = models.CharField(max_length=5,choices=Duration_choices,default='1')
	ScheduledStartTime = models.TimeField(null=True,blank=True)
	ScheduledEndTime = models.TimeField(null=True,blank=True)
	TimeSettings = models.CharField(max_length=5,choices=Event_Timings,default='B')
	EndTime = models.TimeField(null=True,)
	EndDate = models.DateField(null=True,blank=True,default=date.today)
	DeadLineTime = models.TimeField(null=True,blank=True,default="23:30:00")
	DeadLineDate = models.DateField(null=True,blank=True,default=defaultDeadLine)
	Priority = models.CharField(max_length=5,choices=Priority_Options,default='1')
	Type = models.CharField(max_length=5,choices=Event_Type,default='E')
	Completed = models.BooleanField(default=False)
	def __str__(self):
		return self.name

## A model for slots
# @details It has a field a Day_Sched that has a foreignkey to the model DailySched. The EventConnected
# field has a foreign key to the Event model, to store the event in the specific slot.
class Slots(models.Model):
	UserProfile = models.ForeignKey(profile, on_delete=models.CASCADE)
	Day_Sched = models.ForeignKey(DailySched, on_delete=models.CASCADE)
	StartTime = models.TimeField(null=False,blank=False)
	EndTime = models.TimeField(null=False,blank=False)
	SlotNum= models.IntegerField(null=False,blank=False)
	EventConnected = models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
	def __str__(self):
		return str(self.SlotNum)

## A model for exams given by instructors
# @details This model will save the instance of an exam scheduled by instructor related to a course
# Student enrolled can use this model and autogenerate time for their study as well as sweep of time
# when rthe exam is scheduled
class InstructorExam(models.Model):
	UserProfile = models.ForeignKey(profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	Description = models.CharField(max_length=300,blank=True)
	Venue = models.CharField(max_length=100,blank=True)
	StartTime = models.TimeField(null=True,)
	Date = models.DateField(null=True,default=date.today)
	EndTime = models.TimeField(null=True,)
	PreparationDuration = models.CharField(null=True,max_length=5,choices=Duration_choices,default='1',blank=True)

## A model for classes scheduled by the instructor
# @details A class scheduled that can convert to an indespensible event for the student
class InstructorClass(models.Model):
	UserProfile = models.ForeignKey(profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	Description = models.CharField(max_length=300,blank=True)
	Venue = models.CharField(max_length=100,blank=True)
	StartTime = models.TimeField(null=True,)
	Date = models.DateField(null=True,default=date.today)
	EndTime = models.TimeField(null=True,)
	Compulsory = models.BooleanField(default=True)

## A model for assignments given by the instrtuctor
# @details Assignment planned by instructor to be done before a given deadline time
# Also it contains the expectation of student as well as will be showing suggestion of peers while scheduling this into an event
class InstructorAssignment(models.Model):
	UserProfile = models.ForeignKey(profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	Description = models.CharField(max_length=300,blank=True)
	StartTime = models.TimeField(null=True,)
	StartDate = models.DateField(null=True,default=date.today)
	ExpectedDuration = models.CharField(max_length=5,choices=Duration_choices,default='1')
	DeadLineTime = models.TimeField(null=True,blank=True,default="23:30:00")
	DeadLineDate = models.DateField(null=True,blank=True,default=defaultDeadLine)
