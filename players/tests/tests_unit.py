import json
from django.test import TestCase

from mixer.backend.django import mixer

PLAYERS_QUERY = '''
 {
   players {
     picture
     gender
     motto
   }
 }
'''

UPDATE_PLAYER_MUTATION = '''
 mutation editPlayerMutation($id: ID, $motto: String) {
     updatePlayer(id: $id, motto: $motto, picture: $motto, gender: "MALE") {
         player {
            picture
            gender
            motto
        }
     }
 }
'''


from graphene_django.utils.testing import GraphQLTestCase
from players.schema import schema
from players.models import Player


class PlayerUnitTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema 
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        self.player1 = mixer.blend(Player)
        self.player1 = mixer.blend(Player)

    def test_players_response(self):
        response = self.query(
            PLAYERS_QUERY, #op_name="player"
        )

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
        assert len(content["data"]["players"]) == 2

    def test_update_player_response(self):
        response = self.query(
            UPDATE_PLAYER_MUTATION,
            op_name="editPlayerMutation",
            variables={"id": self.player1.user.id, "motto": "YOLO"}
        )
        self.assertResponseNoErrors(response)
