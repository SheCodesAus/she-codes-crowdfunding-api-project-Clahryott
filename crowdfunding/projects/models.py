from django.contrib.auth import get_user_model
from django.db import models

### create your models here and for every model, create a serializer

User = get_user_model() #its using from setting.py - it's telling it to go there // added to use the user.

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    goal = models.IntegerField() #this needs a minimum amount, such as 1 - is this correct? ###
    image = models.URLField()
    is_open = models.BooleanField() #another way this could be is = is_active or status
    date_created = models.DateTimeField(auto_now_add=True) # auto_now_add=True --- this updates to time created
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_projects') #the section in () connects the owner ID to the related name = owner_projects
    liked_by = models.ManyToManyField(User,related_name='liked_projects')

    #@property
    #def total(self):
    #	return self.pledges.aggregate(sum=models.Sum('amount'))['sum']

    @property
    def amount_pledged(self):       
        '''    Calculates the total of each pledge for each project.   '''
        pledge_amount = self.pledges.aggregate(sum=models.Sum('amount'))['sum']
        if pledge_amount == None:
            return 0
        else:
            return pledge_amount 

    @property
    def goal_vs_pledges(self):    
        '''    Looks at the goal and compares to the total number of pledges. '''
        goal_balance = self.goal - self.amount_pledged
        
        if goal_balance <= 0:
            return f"Congratulations! {self.title} project has been funded with {self.amount_pledged} worth of pledges!"
        else:
            return f"There's {goal_balance} left to raise until the goal of {self.goal} is reached!"
    
    def __str__(self):
        '''     Changing representation of project object id to title so when ModelSerializer form is rendered, the title of the project will display, not the ID number.
                Same way as in admin portal from django project    '''  #does this work? #####
        return self.title

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pledges') #FK triggers a rename to a No# - such as support project will be project ID
    supporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supporter_pledges') #what is cascade and on-delete  - it does a mass delete??? confirm  

# Can ADD COMMENT FUNCTION if you have time and want