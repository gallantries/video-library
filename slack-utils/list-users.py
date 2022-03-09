#!/usr/bin/env python
import argparse
import json
import os
from slack_bolt import App
import time
import lib


app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@lib.persist_to_file("users.json")
def list_users():
    members = []
    cid = None
    while True:
        try:
            r = app.client.users_list(limit=500, cursor=cid)
            print(len(r.data['members']))
            members += r.data['members']
            cid = r.data['response_metadata']['next_cursor']
            if cid == "" or cid is None:
                break

        except KeyError:
            break
    return members

tz = {}
for member in list_users():
    t = member.get('tz_offset', 0) / 3600
    if t not in tz:
        tz[t] = 0
    tz[t] += 1

__import__('pprint').pprint(tz)
