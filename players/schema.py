import graphene

from .types import PlayerType, PlayerBoardType
from .models import Player, PlayerBoard


class Query(graphene.ObjectType):
    players = graphene.List(PlayerType) 

    def resolve_players(self,*args, **kwargs):
        return Player.objects.all().order_by("id")


class Mutation(graphene.ObjectType):
    pass 

schema = graphene.Schema(query=Query)  #, mutation=Mutation)
