#!/usr/bin/env python
import shutil
import requests
import datetime
import os
import sys
import glob
import time
import markdown2mrkdwn

NOW = datetime.datetime.now().astimezone()
folder, slack_url = sys.argv[1:]


for fn in sorted(glob.glob(os.path.join('scheduled', folder, '*.md'))):
    # Parse out the date
    parts = fn.split('/') # not os generic
    timestamp = parts[-1][0:24]
    parsed = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')

    if parsed > NOW:
        continue

    with open(fn, 'r') as handle:
        blocks = markdown2mrkdwn.convert_text(handle.read())

    r = requests.post(slack_url, json=blocks)

    if r.text == "ok":
        shutil.move(fn, os.path.join('sent', *parts[1:]))
    else:
        print(r.text)
