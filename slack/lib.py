import yaml

with open('video-library.yaml', 'r') as handle:
    VIDEOS = yaml.safe_load(handle)

with open('sessions.yaml', 'r') as handle:
    SESSIONS = yaml.safe_load(handle)


def convert_name(path):
    path_parts = path.split('/')
    if path_parts[0] == 'statistics':
        path_parts[0] = 'machine_learning'
    if path_parts[0] == 'sequence-analysis':
        path_parts[0] = 'ngs'

    if 'galaxy/intro' in path or path_parts[0] == 'introduction':
        return 'galaxy-intro'
    elif path_parts[0] in ('galaxy', 'community', 'webinar'):
        return 'general'
    elif path_parts[0] == 'course':
        # These are specific to their events
        return '-'.join(['event', path_parts[1].replace('welcome-', '')])
    elif path_parts[0] == 'contributing':
        return 'gtn'
    elif 'tool-generators' in path_parts[1]:
        return 'dev-toolfactory'
    elif len(path_parts) > 2 and path_parts[2] in ('tutorial', 'slides'):
        return "_".join(path_parts[0:2])
    elif len(path_parts) > 2:
        return "_".join(path_parts[0:2])
    elif len(path_parts) == 2:
        return "_".join(path_parts[0:2])
    return None


def get_managed_channels():
    channels = []
    for k, v in VIDEOS.items():
        old_name = v.get('old_support_channel', None)
        override = v.get('support_channel', None)
        new_name = convert_name(k).lower()

        if override is not None:
            channels.append(override)
        else:
            channels.append(new_name)
    return sorted(list(set(channels)))


def get_managed_channels_with_resources():
    channels = {}
    for k, v in VIDEOS.items():
        old_name = v.get('old_support_channel', None)
        override = v.get('support_channel', None)
        new_name = convert_name(k).lower()

        if override is not None:
            name = override
        else:
            name = new_name

        if name not in channels:
            channels[name] = []

        channels[name].append(k)

    return channels


def get_managed_channels_with_resources_sessions():
    INVERTED_SESSIONS = {}
    for k, v in SESSIONS.items():
        for vid in v['videos']:
            INVERTED_SESSIONS[vid] = k

    CHANNEL_MAPPING = {}
    for k, v in VIDEOS.items():
        if 'support_channel' in v:
            c = v['support_channel']
        else:
            c = convert_name(k)

        if c not in CHANNEL_MAPPING:
            CHANNEL_MAPPING[c] = []

        if k in INVERTED_SESSIONS:
            CHANNEL_MAPPING[c].append('session:' + INVERTED_SESSIONS[k])
        else:
            CHANNEL_MAPPING[c].append('video:' + k)

    CHANNEL_MAPPING = {k: list(set(v)) for k, v in CHANNEL_MAPPING.items()}
    return CHANNEL_MAPPING
