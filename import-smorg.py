#!/usr/bin/env python
import copy
import yaml
import sys

data = yaml.load(open(sys.argv[1], 'r'))

videos = {}
sessions = {}

def listify(d):
    if isinstance(d, list):
        return d

    return [d]


def getkey(v, mat):
    if mat['link'].startswith('topics/'):
        s = mat['link'].split('/')
        return s[1] + '/' + s[2] + '/' + mat['type']
    else:
        return v['name'] + mat['type']


def process(v):
    versions = [{
        'link': v['video'].get('link', None),
        'length': v['video'].get('length', None),
        'speakers': listify(v.get('speaker', [])),
        'captions': listify(v['video'].get('captions', [])),
        'date': '2021-02-15',
        'galaxy_version': '21.01',
    }]
    fixmats = []
    for material in v.get('material', []):
        if material['type'] == 'Slides':
            fixmats.append(material)
        elif material['type'] == 'Tutorial':
            fixmats.append(material)
        else:
            print(f"Dunno what to do with {material['type']}")

    n = {
        'description': v['description'],
        'support_channel': v.get('support_channel', None),
        'support_link': v.get('support_link', None),
        'faq': v.get('faq', None),
        'type': v.get('type', None),
        'tags': [],
        # 'language': ,
        'versions': versions,
        # 'material': materials,
        # 'supported_servers': [],
    }
    for mat in fixmats:
        n['materials'] = [mat]
        k = getkey(v, mat)
        videos[k] = copy.deepcopy(n)

    if len(fixmats) == 0:
        videos[v['name']] = copy.deepcopy(n)


for k, v in data.items():
    if 'sessions' in v:
        print(k)
        for vv in v['sessions']:
            if 'videos' in vv:
                for video in vv['videos']:
                    vv['video'] = video
                process(vv)


with open('videos.yaml', 'a') as handle:
    yaml.dump(videos, handle)
