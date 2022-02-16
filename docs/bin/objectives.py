#!/usr/bin/env python
import glob
import json

objectives = {}
gtn = {}

for fn in glob.glob("_data/gtn_*.json"):
    with open(fn, 'r') as handle:
        data = json.load(handle)

        for material in data['materials']:
            k = material['topic_name'] + '/' + material['tutorial_name']

            if material.get('slides', False):
                objectives[k + '/slides'] = material.get('objectives', [])
                gtn[k + '/slides'] = material['title']

            if material.get('hands_on', False):
                objectives[k + '/tutorial'] = material.get('objectives', [])
                gtn[k + '/tutorial'] = material['title']

with open('_data/gtn.json', 'w') as handle:
    json.dump(gtn, handle, ensure_ascii=False)

with open('_data/objectives.json', 'w') as handle:
    json.dump(objectives, handle, ensure_ascii=False)
