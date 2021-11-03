from django.db import models
from Doctors.models import Doctor

class Listing(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING,default=0)
    state = models.CharField(max_length=100)
   
    def __STR__(self):
        return self.state