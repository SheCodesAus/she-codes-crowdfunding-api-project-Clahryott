from django.contrib import admin
from .models import Pledge, Project

# Register your models here.

admin.site.register(Project)
admin.site.register(Pledge)