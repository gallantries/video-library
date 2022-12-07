#!/usr/bin/env python
import json
import requests

modules = requests.get('http://localhost:4000/video-library/api/modules.json').json()
videos = requests.get('http://localhost:4000/video-library/api/videos.json').json()
videos = requests.get('http://localhost:4000/video-library/api/videos.json').json()
sessions = requests.get('http://localhost:4000/video-library/api/sessions.json').json()
instructors = requests.get('http://localhost:4000/video-library/api/instructors.json').json()
instructors = requests.get('http://localhost:4000/video-library/api/instructors.json').json()

topics = requests.get('http://localhost:4002/training-material/api/topics.json').json()
materials = {}
for k, v in topics.items():
	topic_data = requests.get(v['url']).json()
	for material in topic_data['materials']:
		materials[material['url'][1:]] = material

eu_tools = [x['id'] for x in json.load(open('eu.json', 'r'))]
au_tools = [x['id'] for x in json.load(open('au.json', 'r'))]
us_tools = [x['id'] for x in json.load(open('us.json', 'r'))]
fr_tools = [x['id'] for x in json.load(open('fr.json', 'r'))]
be_tools = [x['id'] for x in json.load(open('be.json', 'r'))]


def m2l(mats):
	if mats is None:
		return []

	for m in mats:
		if 'link' in m and 'external' not in m:
			yield "https://training.galaxyproject.org/" + m['link']

def s2n(speakers):
	for speaker in speakers:
		yield instructors[speaker].get('name', speaker)


columns = [
	'Module',
	'Session',
	'Title',
	'Type',
	'Speakers',
	'Materials',
	'Status',
	'Tags',
	'Length',
	'Link',
	'YouTube Checklist',
	'Captions',
	'Website',
	'Final Check',
	'Notes',
	'WFs',
	'WF Tests',
	'EU',
	'AU',
	'US',
	'FR',
	'BE',
]

def find_tool(tool, server):
	tool = tool.replace('%2F', '/')
	if tool in server:
		return 'Exact'
	else:
		if '/' not in tool:
			possible = [x for x in server if '/' in x and tool == x.split('/')[4]]
			if len(possible) > 0:
				return 'Latest'
			else:
				return 'None'
		else:
			# Version mismatch?
			possible = sorted([x.split('/')[5] for x in server if '/' in x and '/'.join(tool.split('/')[0:5]) == '/'.join(x.split('/')[0:5])])[::-1]
			if len(possible) == 0:
				return 'Unavailable!'
			else:
				tool_version = tool.split('/')[5]
				return f"E: {tool_version} O: {possible}"


def determine_support(module, video):
	has_workflows = False
	has_wf_tests = False

	if 'Tutorial' not in video['type']:
		return [has_workflows, has_wf_tests, 'N/A', 'N/A', 'N/A']
	
	if module == 'Galaxy Admin Training':
		return [has_workflows, has_wf_tests, 'N/A', 'N/A', 'N/A']

	if len(v.get('materials', [])) == 0:
		return [has_workflows, has_wf_tests, 'Missing Materials', 'Missing Materials', 'Missing Materials']

	eu_supports = []
	au_supports = []
	us_supports = []
	fr_supports = []
	be_supports = []
	for mat in [x for x in v['materials'] if x['type'] == 'Tutorial']:
		print(mat['link'])
		tools = materials[mat['link']]['tools']
		for tool in tools:
			eu_supports.append(f"{tool} {find_tool(tool, eu_tools)}")
			au_supports.append(f"{tool} {find_tool(tool, au_tools)}")
			us_supports.append(f"{tool} {find_tool(tool, us_tools)}")
			fr_supports.append(f"{tool} {find_tool(tool, fr_tools)}")
			be_supports.append(f"{tool} {find_tool(tool, be_tools)}")

		wfs = materials[mat['link']].get('workflows', [])
		if len(wfs) > 0:
			has_workflows = True
		if any([x['tests'] for x in wfs]):
			has_wf_tests = True

	return [
		has_workflows, 
		has_wf_tests, 
		"\n".join(eu_supports),
		"\n".join(au_supports),
		"\n".join(us_supports),
		"\n".join(fr_supports),
		"\n".join(be_supports),
		]

def emit(module, session, v):
	return [
		module,
		session,
		v['title'],
		v['type'],
		# data['description'],
		", ".join(s2n(v.get('speakers', []))),
		"\n".join(m2l(v.get('materials', []))),
		"TO REVIEW",
		# "Also included in",
		", ".join(v['tags']),
		v['length'],
		"https://youtu.be/" + v['link'],
		'FALSE', # YouTube Checklist
		'FALSE', # Captions
		'FALSE', # Website update
		'FALSE', # Website checked by speaker
		'', # Notes
	] + determine_support(module, v)

has_emitted_row = {}
import csv
csvwriter = csv.writer(open('out.csv', 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(columns)
for module_id, module in modules.items():
	# print(v)

	for k2, v2 in module['program'].items():
		# Section
		if 'trainings' not in v2:
			continue

		for item in v2['trainings']:

			if 'video' in item:
				vk = item['video']
				if vk in has_emitted_row:
					continue
				else:
					has_emitted_row[vk] = True
				v = videos[vk]
				v.update(v['versions'][0])

				row = emit(
					module['title'],
					"",
					v
				)
				csvwriter.writerow(row)

			elif 'session' in item:
				sesh = sessions[item['session']]
				for vk in sesh['videos']:
					if vk in has_emitted_row:
						continue
					else:
						has_emitted_row[vk] = True

					v = videos[vk]
					v.update(v['versions'][0])
					row = emit(
						module['title'],
						sesh['title'],
						v
					)
					csvwriter.writerow(row)
			else:
				pass


	# {'layout': 'module', 'title': 'Sequence Analysis Basics', 'description': 'This modules covers the basics of sequence analysis, including Quality Control (QC), mapping, and genome assembly.', 'program': {'intro': {'trainings': [{'session': 'sequence-analysis/quality-control'}, {'session': 'sequence-analysis/mapping'}, {'session': 'assembly'}]}}, 'url': 'http://0.0.0.0:4000/video-library/api/modules/sequence-analysis-basics.json'}

