import graphene
from graphene_django.rest_framework.mutation import SerializerMutation


from .types import PlayerType
from .models import Player
from .serializers import PlayerSerializer


class CreatePlayerMutation(SerializerMutation):
    class Meta:
        serializer_class = PlayerSerializer


class EditPlayerMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        picture = graphene.String()
        gender = graphene.String()
        birthday = graphene.String()
        motto = graphene.String()

    player = graphene.Field(PlayerType)

    def mutate(self, info, id, picture, gender, motto):
        player = Player.objects.get(pk=id)
        player.picture = picture 
        player.gender = gender 
        # player.birthday = birthday
        player.motto = motto 
        player.save()

        return EditPlayerMutation(player=player)
        
