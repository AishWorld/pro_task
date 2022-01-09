from django.contrib import admin

# Register your models here.
from taskapp.models import Person, Employee

admin.site.register([Employee,Person])