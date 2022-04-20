# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['PlayerSnapshotCase::test_api_players_snapshot 1'] = {
    'data': {
        'players': [
            {
                'gender': None,
                'motto': '''Task hard too star relate oil. Time imagine number crime.
Page statement form between ball decision. Hold himself only.''',
                'picture': 'Remember history type education page ground hot. Trial window very become current notice new image.'
            }
        ]
    }
}

snapshots['PlayerSnapshotCase::test_api_update_player_snapshot 1'] = {
    'data': {
        'updatePlayer': {
            'player': {
                'gender': 'MALE',
                'motto': 'YOLO',
                'picture': 'YOLO'
            }
        }
    }
}
