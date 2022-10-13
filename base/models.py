import email
from email.policy import default
from django.db import models

# Create your models here.
class forminput(models.Model):
    email = models.EmailField()
    audiences = models.IntegerField(default= 1)
    ageranges = models.CharField(max_length = 4, default = -1)
    gp = models.CharField(max_length = 60, default = -1)
    recommendations = models.CharField(max_length = 600, default = -1)
