from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.TextField(blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    motto = models.TextField(blank=True)
    board = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self) -> str:
        return str(self.id)


class PlayerBoard(models.Model):

    def __str__(self) -> str:
        return str(self.id)
