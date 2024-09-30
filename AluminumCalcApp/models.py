from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

class Tolerance12_2Model(models.Model):
    diameter_range_from = models.IntegerField()
    diameter_range_to = models.IntegerField()
    allowable_deviation_mean_diameter_5k = models.IntegerField()
    allowable_deviation_mean_diameter_other = models.IntegerField()
    allowable_deviation_point_diameter_5k = models.IntegerField()
    allowable_deviation_point_diameter_other = models.IntegerField()

class UserTolerances12_2Model(models.Model):
    name = models.CharField(max_length=100)
    alloy = models.CharField(max_length=100)
    diameter = models.IntegerField()
    tolerance1 = models.IntegerField()
    class Meta:
        db_table = "UserTolerances12_2"