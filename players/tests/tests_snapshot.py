from snapshottest import TestCase
from graphene.test import Client

from mixer.backend.django import mixer

from players.schema import schema
from players.models import Player
from players.tests.tests_unit import PLAYERS_QUERY, UPDATE_PLAYER_MUTATION


class PlayerSnapshotCase(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.player1 = mixer.blend(Player)


    def test_api_players_snapshot(self):
        response = self.client.execute(PLAYERS_QUERY)
        self.assertMatchSnapshot(response)

    def test_api_update_player_snapshot(self):
        response = self.client.execute(
            UPDATE_PLAYER_MUTATION, variables={
                'id': self.player1.user.id, 'motto': 'YOLO'
            }
        )
        self.assertMatchSnapshot(response)
