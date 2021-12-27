from django.db import models


class Post(models.Model):
    unit_name = models.IntegerField(max_length=100)
    year = models.IntegerField(max_length=100)
    dacoity = models.IntegerField(max_length=100)
    robbery = models.IntegerField(max_length=100)
    murder = models.IntegerField(max_length=100)
    speedy_trial = models.IntegerField(max_length=100)
    riot = models.IntegerField(max_length=100)
    wcrepresion = models.IntegerField(max_length=100)
    kidnapping = models.IntegerField(max_length=100)
    policeassult = models.IntegerField(max_length=100)
    burglary = models.IntegerField(max_length=100)
    theft = models.IntegerField(max_length=100)
    othercases = models.IntegerField(max_length=100)
    armsact = models.IntegerField(max_length=100)
    explosive = models.IntegerField(max_length=100)
    nacrotics = models.IntegerField(max_length=100)
    smuggling = models.IntegerField(max_length=100)
