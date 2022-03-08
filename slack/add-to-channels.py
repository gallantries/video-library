#!/usr/bin/env python
import tqdm
import argparse
import json
import os
from slack_bolt import App
import time
import lib


app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@lib.persist_to_file("conversations.json")
def list_conversations():
    conversations = app.client.conversations_list(limit=400).data
    return conversations



parser = argparse.ArgumentParser(description='Add users to specific channels')
parser.add_argument('users', type=str, nargs='+',
                    help='Slack User IDs')
parser.add_argument('--channels', choices=('all', 'admin_', 'managed', 'galaxy_'), type=str, help="Which groups of channels to add the user to")
args = parser.parse_args()


conversations = list_conversations()
channels = []
if args.channels == 'all':
    channels = [x for x in conversations['channels'] if x['is_archived'] is False]
elif args.channels == 'admin_':
    channels = [x for x in conversations['channels'] if x['is_archived'] is False and x['name'].startswith('admin_')]
elif args.channels == 'galaxy_':
    channels = [x for x in conversations['channels'] if x['is_archived'] is False and x['name'].startswith('galaxy-')]
elif args.channels == 'managed':
    managed = lib.get_managed_channels()
    channels = [x for x in conversations['channels'] if x['is_archived'] is False and x['name'] in managed]

for channel in tqdm.tqdm(channels):
    print(channel)
    try:
        app.client.conversations_invite(channel=channel['id'], users=','.join(args.users))
    except Exception as sae:
        print(sae)

    time.sleep(2)
