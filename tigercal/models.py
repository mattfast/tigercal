from django.db import models

class Student(models.Model):
	username = models.CharField(max_length=100)

class Group(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

class Membership(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Leadership(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Event(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	is_public = models.BooleanField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	descrip = models.TextField()