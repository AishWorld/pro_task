from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length=200)
    created_datetime = models.DateTimeField(auto_now=True, null=True)
    modified_datetime = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
# person_id Foreign Key, department, role, line_manager person_id Foreign Key, created datetime, modified datetime
class Employee(models.Model):
    person_id = models.ForeignKey(Person,on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    