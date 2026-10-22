from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)  
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=60)

    def __str__(self):
        return self.name
