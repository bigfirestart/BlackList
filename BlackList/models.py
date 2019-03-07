from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Item(models.Model):
     name = models.CharField(max_length=100,default = "None")
     reason = models.CharField(max_length=200)
     anger_procent = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
     date = models.DateField(auto_now=True)
class Offender(models.Model):
    name = models.CharField(max_length=100,default = "None")
    def __str__(self):
        return self.name
