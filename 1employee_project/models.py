from django.db import models

# Create your models here.


#  we create two models one for position and another for employee and we reference position to 
#  employee table using foreign key. each model means one table 

class Position(models.Model):
    title = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    mobile = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    