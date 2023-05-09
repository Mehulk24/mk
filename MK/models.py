from django.db import models

# Create your models here.

class contact(models.Model):
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    msg=models.TextField()
    
def __str__(self):
    return self.fname
