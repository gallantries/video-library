#!/usr/bin/env python
import time
import requests
import json
import yaml
import lib
import os

SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']


with open('instructors.yaml', 'r') as handle:
    INSTRUCTORS = yaml.safe_load(handle)
    INSTRUCTORS_WITH_SLACK = {k: v['slack'] for (k, v) in INSTRUCTORS.items() if 'slack' in v}
    GALLANTRIES_INSTRUCTORS = [v['slack'] for (k, v) in INSTRUCTORS.items() if 'gallantries' in v.get('affiliation', []) and 'slack' in v]

with open('video-library.yaml', 'r') as handle:
    data = yaml.safe_load(handle)


app = lib.app
conversations = lib.list_channels()


def find_channel_by_name(channel):
    named = [x for x in conversations if x['name'] == channel and not x['is_archived'] ]
    old = [x for x in conversations if channel in x['previous_names'] and not x['is_archived'] ]
    if len(named) == 1:
        return named[0]
    elif len(old) > 0:
        return None
    else:
        return None


for k, v in data.items():
    override = v.get('support_channel', None)
    new_name = lib.convert_name(k).lower()

    name = override.lstrip('#') if override is not None else new_name.lstrip('#')

    if 'event-' in new_name:
        continue


    if find_channel_by_name(name) is None:
        print(f"Creating a new channel {name}")
        channel = app.client.conversations_create(name=new_name)
        cid = channel['channel']['id']
        time.sleep(5)

        # Invite all of the gallantries users by default
        contributors = [y.get('captions', []) + y.get('speakers', []) for y in v['versions']]
        contributors = [item for sublist in contributors for item in sublist]
        contributors = list(set(contributors))
        contributors_slack = [INSTRUCTORS_WITH_SLACK.get(x) for x in contributors]
        contributors_slack = [x for x in contributors_slack if x is not None]

        total_users = GALLANTRIES_INSTRUCTORS + contributors_slack
        app.client.conversations_invite(channel=cid, users=','.join(total_users))
        time.sleep(2)
