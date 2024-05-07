from django.db import models

# Define models for Parent, Child, Hospital, Appointment, etc.
# For example:

class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields as needed

class Child(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    # Add other fields as needed
