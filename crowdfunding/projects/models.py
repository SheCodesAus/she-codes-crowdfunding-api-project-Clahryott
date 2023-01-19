from django.contrib.auth import get_user_model
from django.db import models

#create your models here and for every model, create a serializer

User = get_user_model() #its using from setting.py - it's telling it to go there // added to use the user..?


class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	goal = models.IntegerField()
	image = models.URLField()
	is_open = models.BooleanField() #another way is is_active or status
	date_created = models.DateTimeField(auto_now_add=True) # auto_now_add=True --- this updates to time created
	#owner = models.CharField(max_length=200) --- NO LONGER USED
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_projects') #the section in () connects the owner ID to the owner_projects


class Pledge(models.Model):
	amount = models.IntegerField()
	comment = models.CharField(max_length=200)
	anonymous = models.BooleanField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pledges') #foreign key triggers a rename to a No# - such as support project will be project ID
	supporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supporter_pledges') #what is cascade and on-delete  - it does a mass delete??? confirm  

