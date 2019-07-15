from django.db import models

# Create your models here.
class Game(models.Model):
    firstGame = models.CharField(max_length=120, default="")
    secondGame = models.CharField(max_length=120, default="",blank=True)
    thirdGame = models.CharField(max_length=120, default="",blank=True)