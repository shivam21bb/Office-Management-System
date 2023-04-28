from django.db import models

# Create your models here.cl
class Department(models.Model):
    name=models.CharField(max_length=70 ,null=False)
    location=models.CharField(max_length=70,null=False)
class Role(models.Model):
    name=models.CharField(max_length=70 ,null=False)
class Employee(models.Model):
    first_name=models.CharField(max_length=70,null=False)
    last_name=models.CharField(max_length=70)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salarly=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()

