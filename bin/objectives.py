#!/usr/bin/env python
import sys
import json

objectives = {}
studyload = {}
gtn = {}
supported = {}

for fn in sorted(sys.argv[1:]):
    with open(fn, 'r') as handle:
        data = json.load(handle)

        for material in data['materials']:
            k = material['topic_name'] + '/' + material['tutorial_name']

            gtn[k] = material['title']
            studyload[k] = material.get('time_estimation', None)
            supported[k] = material.get('supported_servers', None)

            if material.get('slides', False):
                objectives[k + '/slides'] = material.get('objectives', [])

            if material.get('hands_on', False):
                objectives[k + '/tutorial'] = material.get('objectives', [])
                supported[k + '/tutorial'] = material.get('supported_servers', None)

with open('_data/gtn.json', 'w') as handle:
    json.dump(gtn, handle, ensure_ascii=False, sort_keys=True, indent=2)

with open('_data/objectives.json', 'w') as handle:
    json.dump(objectives, handle, ensure_ascii=False, sort_keys=True, indent=2)

with open('_data/studyload.json', 'w') as handle:
    json.dump(studyload, handle, ensure_ascii=False, sort_keys=True, indent=2)

with open('_data/supported.json', 'w') as handle:
    json.dump(supported, handle, ensure_ascii=False, sort_keys=True, indent=2)
