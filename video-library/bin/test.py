import yaml

with open('_data/videos.yaml', 'r') as handle:
    data = yaml.safe_load(handle)

for k, v in data.items():
    t = k.split('/')[0]
    if t not in v['tags']:
        v['tags'].append(t)
    if 'description' in v and v['description'] is not None:
        v['description'] = " ".join(v.get('description', '').strip().split('\n'))

with open('_data/videos.yaml', 'w') as handle:
    yaml.dump(data, handle)
