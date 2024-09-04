from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=128)
    university = models.ManyToManyField(Program, through="Eligibility")

    def __str__(self):
        return self.name

class Eligibility(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    college = models.CharField(max_length=128)