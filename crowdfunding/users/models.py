from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# abstract user to return user name as a string of the database raw name.
class CustomUser(AbstractUser):
    # add project models to use the user ***

    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    profile_picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username
