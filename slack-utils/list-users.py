#!/usr/bin/env python
import argparse
import json
import os
from slack_bolt import App
import time
import lib


app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

tz = {}
for member in lib.list_users(app):
    t = member.get('tz_offset', 0) / 3600
    if t not in tz:
        tz[t] = 0
    tz[t] += 1

__import__('pprint').pprint(tz)
