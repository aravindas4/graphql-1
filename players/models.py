from django.db import models
from django.contrib.auth.models import User

class PlayerBoard(models.Model):
    points = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    board = models.ForeignKey(
        PlayerBoard, on_delete=models.CASCADE, related_name="players", null=True
    )
    picture = models.TextField(blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    motto = models.TextField(blank=True)


    def __str__(self) -> str:
        return str(self.id)



