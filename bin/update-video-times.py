#!/usr/bin/env python
import yaml
import subprocess
import json

with open('_data/videos.yaml', 'r') as handle:
    data = yaml.safe_load(handle)


def convertTime(n):
    if n >= 60 * 60:
        q = n // 60
        s = n % 60
        n2 = n // 60
        h = n2 // 60
        m = n2 % 60
        if m == 0:
            return f"{h}H"
        else:
            return f"{h}H{m}M"
    elif n > 60:
        m = n // 60
        s = n % 60
        return f"{m}M"
    else:
        return f"{n}S"


for k, v in data.items():
    if len(v.get('versions', [])):
        for video in v['versions']:
            print(k, video)
            if True: # video['length'] is None or len(video['length'].strip()) == 0:
                print(video['link'])
                out = subprocess.check_output(['youtube-dl', '-j', '--', video['link']]).decode('utf-8')
                out = json.loads(out)
                duration = int(out['duration'])
                video['length'] = convertTime(duration)

with open('_data/videos.yaml', 'w') as handle:
    yaml.dump(data, handle)
