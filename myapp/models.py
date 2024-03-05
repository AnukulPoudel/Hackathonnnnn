from django.db import models

# User input: complaint name, complaint description
# Create your models here.
class Complaint(models.Model):
    complaintName = models.CharField(max_length=200)
    complaintDiscri = models.CharField(max_length=1000)
