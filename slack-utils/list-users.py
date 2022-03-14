#!/usr/bin/env python
from collections import Counter
import argparse
import json
import time
import lib



tz = {}
emoji = Counter()
for member in lib.list_users():
    t = member.get('tz_offset', 0) / 3600
    if t not in tz:
        tz[t] = 0
    tz[t] += 1

    if 'profile' in member:
        if 'status_emoji' in member['profile']:
            emoji[member['profile']['status_emoji']] += 1

__import__('pprint').pprint(tz)

__import__('pprint').pprint(emoji)
