from django.db import models

# Create your models here.
class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    points = models.IntegerField(primary_key=False)

    def __str__(self) -> str:
        return  self.id+self.name+self.lastname+self.points