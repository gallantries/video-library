#!/usr/bin/env python
import requests
import yaml
from multiprocessing import Pool
GTN = "https://training.galaxyproject.org/training-material/"
data = yaml.load(open('video-library.yaml', 'r'))
urls = []

for k, v in data.items():
    for m in v.get('materials', []):
        if 'external' in m:
            url = m['link']
        else:
            url = GTN + m['link']

        urls.append((
            k,
            url,
            m['link'],
        ))

        # r = requests.get(url)
        # if r.status_code == 200:
            # continue
        # print(r.status_code)


def fetch(args):
    (material, link, orig) = args
    r = requests.get(link, allow_redirects=False)

    if 'meta http-equiv="refresh"' in r.text:
        # <meta http-equiv="refresh" content="0; url=https://training.galaxyproject.org/training-material/topics/single-cell/tutorials/scrna-intro/slides-plain.html">
        try:
            m = [x.strip() for x in r.text.split('\n') if '<meta http-equiv' in x][0]
            fixed_url = m.split()[3].split('=')[1][0:-2]
        except:
            fixed_url = 'UNKNOWN'
        return ["HTML REDIRECT", material, link, orig, fixed_url]
    else:
        return [r.status_code, material, link, orig, None]

with Pool(40) as p:
    # versions = p.map(fetch, [x for x in urls if x[0].startswith('transcriptomics/')])
    versions = p.map(fetch, urls)
    for v in versions:
        if v[0] == 200:
            continue

        if v[0] != 'HTML REDIRECT': continue

        print(v)
        for m in data[v[1]]['materials']:
            if GTN + m['link'] == v[2]:
                m['link'] = v[4][len(GTN):]
                print(m)

with open('video-library.yaml', 'w') as handle:
    yaml.dump(data, handle)
