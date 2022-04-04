#!/usr/bin/env python
import sys
import lib



data = lib.app.client.users_info(user=sys.argv[1]).data
__import__('pprint').pprint(data)

potential_names = [
    data['user']['name'],
    data['user']['real_name'],
    data['user']['profile']['real_name'],
    data['user']['profile']['real_name_normalized'],
    data['user']['profile']['display_name'],
    data['user']['profile']['display_name_normalized'],
    (data['user']['profile']['first_name'] + ' ' + data['user']['profile']['last_name']).strip(),
]
potential_names = list(set(potential_names))

__import__('pprint').pprint(sorted(potential_names, key=lambda x: -len(x)))
