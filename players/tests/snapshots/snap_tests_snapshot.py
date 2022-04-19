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
                'motto': 'Here church write past establish. Enough his arm then media it trouble church. Bar financial young should any upon perform.',
                'picture': '''Blood foreign although character. Will bit institution dark describe.
Free court back green whatever another perform.
Discussion figure rest along none. Indicate and sure four I finish.'''
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
