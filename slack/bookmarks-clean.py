#!/usr/bin/env python
import json
import os
from slack_bolt import App
from lib import convert_name, get_managed_channels
import time


def persist_to_file(file_name):
    def decorator(original_func):
        try:
            print(f"Reading cache from {file_name}")
            cache = json.load(open(file_name, 'r'))
        except (IOError, ValueError):
            cache = {}
        def new_func(*args, **kwargs):
            memk = f"{args}{kwargs}"
            if memk not in cache:
                cache[memk] = original_func(*args, **kwargs)
                print(f"Writing cache to {file_name}")
                json.dump(cache, open(file_name, 'w'))
                time.sleep(1)
            return cache[memk]
        return new_func
    return decorator

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@persist_to_file("conversations.json")
def list_conversations():
    conversations = app.client.conversations_list(limit=400).data
    return conversations


def id_from_channel_name(name):
    conversations = list_conversations()
    flat = [x for x in conversations['channels'] if x['name'] == name]
    return flat[0]['id']

def non_managed_channels():
    managed = get_managed_channels()
    res = []
    for x in list_conversations()['channels']:
        if x['name'] not in managed:
            res.append(x)

    return sorted(res, key=lambda x: x['name'])


def managed_channels():
    managed = get_managed_channels()
    res = []
    for x in list_conversations()['channels']:
        if x['name'] in managed:
            res.append(x)

    return sorted(res, key=lambda x: x['name'])


for convo in managed_channels():
    print(convo['name'])
    if convo['is_archived']:
        continue

    if not convo['is_member']:
        app.client.conversations_join(channel=convo['id'])

    bookmarks = app.client.bookmarks_list(channel_id=convo['id'])
    if len(bookmarks['bookmarks']) > 0:
        print(f"\tRemoving {len(bookmarks['bookmarks'])} bookmarks")
    for mark in bookmarks['bookmarks']:
        app.client.bookmarks_remove(bookmark_id=mark['id'], channel_id=mark['channel_id'])
        time.sleep(5)
    time.sleep(1)

# for NONmanaged_convo in non_managed_channels():
    # print(NONmanaged_convo['name'])

# for convo in sorted(list_conversations()['channels'], key=lambda x: x['name']):
