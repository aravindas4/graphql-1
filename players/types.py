from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User

from .models import Player, PlayerBoard


class UserType(DjangoObjectType):
    class Meta:
        model = User 
        exclude = ("password",)


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player
        fields = ("id", "picture", "gender", "birthday", "motto", "board")


class PlayerBoardType(DjangoObjectType):
    class Meta:
        model = PlayerBoard 
        fields = '__all__'

