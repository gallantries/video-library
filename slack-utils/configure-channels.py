#!/usr/bin/env python
import requests
import json
import yaml
from lib import convert_name
import os

SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']


with open('video-library.yaml', 'r') as handle:
    data = yaml.safe_load(handle)

r = requests.get(
    f'https://slack.com/api/conversations.list?limit=400',
    headers={'Authorization': f'Bearer {SLACK_BOT_TOKEN}'},
)
global conversations
conversations = r.json()['channels']



def find_channel_by_name(channel):
    named = [x for x in conversations if x['name'] == channel and not x['is_archived'] ]
    old = [x for x in conversations if channel in x['previous_names'] and not x['is_archived'] ]
    if len(named) == 1:
        return named[0]
    elif len(old) > 0:
        return None
    else:
        return None


def slack(method, data):
    if 'channel' in data:
        r = requests.post(
            f'https://slack.com/api/conversations.join',
            headers={'Authorization': f'Bearer {SLACK_BOT_TOKEN}'},
            data={'channel': data['channel']}
        )
        response = r.json()

    if method not in ('conversations.rename', 'conversations.archive'):
        r = requests.post(
            f'https://slack.com/api/{method}',
            headers={'Authorization': f'Bearer {SLACK_BOT_TOKEN}'},
            data=data
        )
        response = r.json()
    else:
        response = None

    if method == 'conversations.create':
        conversations.append({
            'name': data['name'],
            'id': response['channel']['id'],
            'previous_names': [],
            'is_archived': False,
        })
    elif method == 'conversations.archive':
        for x in conversations:
            if x['id'] == data['channel']:
                x['is_archived'] = True
    elif method == 'conversations.rename':
        for x in conversations:
            if x['id'] == data['channel']:
                x['name'] = data['name']


for k, v in data.items():
    old_name = v.get('old_support_channel', None)
    override = v.get('support_channel', None)
    new_name = convert_name(k).lower()
    if old_name is not None:
        old_name = old_name.lstrip('#')
    if override is not None:
        override = override.lstrip('#')
    if new_name is not None:
        new_name = new_name.lstrip('#')

    if 'event-' in new_name:
        continue

    #print(k, old_name, override if override is not None else new_name)
    if old_name == new_name:
        pass
    elif not old_name and not override:
        if find_channel_by_name(new_name) is None:
            print(f"Creating a new channel {new_name}")
            slack('conversations.create', {'name': new_name})
        else:
            pass
            # print(f"{new_name} exists already")
    elif old_name and not override:
        print(f"\tMoving {old_name} -> {new_name}")
        if find_channel_by_name(old_name) is not None:
            if find_channel_by_name(new_name) is not None:
                print(f"\t      Archiving {old_name} (write 'discussion continues in #...')")
                slack('chat.postMessage', {
                    'channel': find_channel_by_name(old_name)['id'],
                    'text': f'This channel is being archived during an ongoing cleanup. Please continue the conversation in #{new_name}'
                })
                slack('conversations.archive', {'channel': find_channel_by_name(old_name)['id']})
                print(f"HELENA ARCHIVE {old_name}")
            else:
                print(f"\t      Rename {old_name} -> {new_name}")
                slack('conversations.rename', {
                    'channel': find_channel_by_name(old_name)['id'],
                    'name': new_name
                })
                print(f"HELENA RENAME {old_name} to {new_name}")

        else:
            if find_channel_by_name(new_name) is not None:
                pass # print(f"\t      Nothing to do, {new_name} exists")
            else:
                print(f"\t      Creating {new_name}")
                slack('conversations.create', {'name': new_name})
    elif override is not None:
        if find_channel_by_name(override) is not None:
            pass # print(f"\t      Nothing to do")
        else:
            print(f"\t      Creating {override}")
            slack('conversations.create', {'name': override})
    else:
        print("???")
