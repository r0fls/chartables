from django.db import models
from charts.models import Chartable

class Test(Chartable):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
# Create your models here.
