import graphene

from .types import PlayerType, PlayerBoardType
from .models import Player, PlayerBoard
from .mutations import EditPlayerMutation, CreatePlayerMutation


class Query(graphene.ObjectType):
    players = graphene.List(PlayerType)
    player = graphene.Field(PlayerType, player_id=graphene.Int())
    player_board = graphene.List(PlayerBoardType)

    def resolve_players(self,info, **kwargs):
        return Player.objects.all().order_by("-board__points")

    def resolve_player(self, info, player_id):
        return Player.objects.get(pk=player_id)

    def resolve_player_board(self, info, **kwargs):
        return PlayerBoard.objects.all().order_by("-points")



class Mutation(graphene.ObjectType):
    update_player =  EditPlayerMutation.Field()
    create_player = CreatePlayerMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)