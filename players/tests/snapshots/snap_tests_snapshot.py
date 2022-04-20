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
                'motto': '''Staff analysis I read. Myself he determine respond once field.
Sell throughout look road PM day especially natural. Paper cause heavy serious teacher guy picture.''',
                'picture': '''Professional forward play interview involve seven huge become. During wide sister good college be business. Would spend south may.
Later character news fly without. Side resource data rich.'''
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
