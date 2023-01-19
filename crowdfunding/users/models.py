from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser): #abstract user to return user name as a string of the database raw name. 
# add project models to use the user ***
    pass

    def __str__(self):
        return self.username


