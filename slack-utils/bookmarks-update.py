#!/usr/bin/env python
import json
import os
from slack_bolt import App
from lib import (
    convert_name,
    get_managed_channels,
    get_managed_channels_with_resources,
    get_managed_channels_with_resources_sessions,
    VIDEOS,
    SESSIONS,
)
import time

with open("docs/_data/gtn.json", "r") as handle:
    GTN_TITLES = json.load(handle)


def persist_to_file(file_name):
    def decorator(original_func):
        try:
            print(f"Reading cache from {file_name}")
            cache = json.load(open(file_name, "r"))
        except (IOError, ValueError):
            cache = {}

        def new_func(*args, **kwargs):
            memk = f"{args}{kwargs}"
            if memk not in cache:
                cache[memk] = original_func(*args, **kwargs)
                print(f"Writing cache to {file_name}")
                json.dump(cache, open(file_name, "w"))
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
    flat = [x for x in conversations["channels"] if x["name"] == name]
    return flat[0]["id"]


def non_managed_channels():
    managed = get_managed_channels()
    res = []
    for x in list_conversations()["channels"]:
        if x["name"] not in managed:
            res.append(x)

    return sorted(res, key=lambda x: x["name"])


def bookmarkify(resources):
    for r in resources:
        if r.startswith("session:"):
            sesh_k = r[len("session:") :]
            sesh = SESSIONS[sesh_k]
            yield (
                sesh["title"],
                f"https://gallantries.github.io/video-library/sessions/{sesh_k}/",
            )
        elif r.startswith("video:"):
            vid_k = r[len("video:") :]
            vid = VIDEOS[vid_k]
            print(vid_k)
            if "title" in vid:
                title = vid["title"]
            else:
                vidk2 = "/".join(vid_k.split("/")[0:2])
                title = GTN_TITLES[vidk2]

            yield (
                title,
                f"https://gallantries.github.io/video-library/videos/{vid_k}/",
            )


def managed_channels():
    managed = get_managed_channels_with_resources_sessions()
    res = []
    for x in list_conversations()["channels"]:
        if x["name"] in managed.keys():
            res.append([x, managed[x["name"]]])

    return res


for res in managed_channels():
    (convo, videos) = res
    if convo["is_archived"]:
        continue

    if convo["is_member"] == False:
        app.client.conversations_join(channel=convo["id"])

    print(convo["id"], convo["name"])

    # Planned bookmarks
    new_bookmarks = [
        ("Code of Conduct", "https://galaxyproject.org/community/coc/")
    ] + list(bookmarkify(videos))

    # Get existing bookmarks
    bookmarks = app.client.bookmarks_list(channel_id=convo["id"])
    time.sleep(2)

    existing_urls = set([(x["title"], x["link"]) for x in bookmarks["bookmarks"]])
    new_urls = set(new_bookmarks)

    # To add
    for bmark in new_urls - existing_urls:
        print(f"\t Adding {bmark}")
        app.client.bookmarks_add(
            channel_id=convo["id"], title=bmark[0], type="link", link=bmark[1]
        )
        time.sleep(5)

    # print(bookmarks)

    # links = [('Code of Conduct', 'https://galaxyproject.org/community/coc/')] + list(bookmarkify(videos))
    # print(f"\tAdding {links}")

    # for (title, url) in links:
    # app.client.bookmarks_add(
    # channel_id=convo['id'],
    # title=title,
    # type='link',
    # link=url
    # )

    # CoC
    # Video Library Page Link(s)
