#!/usr/bin/env python
import os
import pytz
import argparse
from datetime import datetime, timedelta
from pytz import timezone
import pytz

IAMHERE = os.path.dirname(os.path.abspath(__file__))

replacements = {
    'Pacific/Auckland': {
        'REGION': 'Asia/Pacific :earth_asia:',
        'BYE_REGION': 'Americas :earth_americas:'
    },
    'Europe/Amsterdam': {
        'REGION': 'Africa/Middle East/Europe :earth_africa:',
        'BYE_REGION': 'Asia/Pacific :earth_asia:'
    },
    'America/New_York': {
        'REGION': 'Americas :earth_americas:',
        'BYE_REGION': 'Europe/Middle East/Africa :earth_africa:'
    },
    'gat': {
        'SOCIAL_CHANNEL': '#event-gat',
        'EVENT': 'GTN Tapas: Galaxy Admin Training',
        'COURSE_WEBSITE': 'https://gallantries.github.io/video-library/events/smorgasbord2/gat.html',
    },
    'gtn': {
        'SOCIAL_CHANNEL': '#social',
        'EVENT': 'GTN Tapas',
        'COURSE_WEBSITE': 'https://gallantries.github.io/video-library/events/smorgasbord2/tapas.html',
    }
}


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--zones', type=str, nargs='+',
                    help='A list of timezones to use', default=['Pacific/Auckland', 'Europe/Amsterdam', 'America/New_York'])
parser.add_argument('start', type=str, help="Start date of the event (required format: YYYY-mm-ddThh:mm:ss)")
parser.add_argument('--days', type=int, help="Number of days of the event", default=5)
parser.add_argument('--course', type=str, help="Which course template to use?", choices=('gat', 'gtn'), default='gtn')
parser.add_argument('outputdir', type=str, help="Folder to write out the messages to (chooses which channel they go into")
args = parser.parse_args()


zones = [timezone(x) for x in args.zones]
# Meh, lazy
earliest_zone = zones[0]

start = datetime.strptime(args.start, '%Y-%m-%dT%H:%M:%S')

if args.days > 2:
    posts = [
        (f'pre-{args.course}.md', start - timedelta(days=3), earliest_zone),
    ]

    for tz in zones:
        posts.append(
            (f'welcome-{args.course}.md', start, tz),
        )

    for tz in zones:
        for i in range(1, args.days - 1):
            posts.append(
                (f'shift-change-{i}-{args.course}.md', start + timedelta(days=i, hours=2), tz)
            )

    for tz in zones:
        posts.append(
            # Sent in evening
            (f'goodbye-{args.course}.md', start + timedelta(days=args.days - 1, hours=4), tz)
        )
else:
    raise Exception()


for post in posts:
    fn, time, tz = post
    localised_time = tz.localize(time)
    print(tz, time, localised_time, fn)

    with open(os.path.join(IAMHERE, fn), 'r') as handle:
        data = handle.read()

    for k, v in replacements[str(tz)].items():
        data = data.replace(f'<{k}>', v)

    for k, v in replacements[args.course].items():
        data = data.replace(f'<{k}>', v)

    with open(os.path.join(args.outputdir, localised_time.strftime('%Y-%m-%dT%H:%M:%S%z') + '-' + fn), 'w') as handle:
        handle.write(data)
