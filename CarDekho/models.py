from django.db import models
from django.core.exceptions import ValidationError

def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError("Only alphanumeric characters are allowed")
    return value

class Showroomlist(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
    
# Create your models here.
class Carlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default = False)
    chassisnumber = models.CharField(max_length=100,blank = True, null = True, validators=[alphanumeric])
    price = models.DecimalField(max_digits=10, decimal_places=2,blank = True, null = True)
    showroom = models.ForeignKey(Showroomlist, on_delete = models.CASCADE,related_name='Showrooms',null = True)
    def __str__(self):
        return self.name
    
