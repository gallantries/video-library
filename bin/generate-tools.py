#!/usr/bin/env python
import json
import requests

modules = requests.get('http://localhost:4000/video-library/api/modules.json').json()
videos = requests.get('http://localhost:4000/video-library/api/videos.json').json()
videos = requests.get('http://localhost:4000/video-library/api/videos.json').json()
sessions = requests.get('http://localhost:4000/video-library/api/sessions.json').json()
topics = requests.get('http://localhost:4002/training-material/api/topics.json').json()
guid = json.load(open('guid-rev.json', 'r'))

materials = {}
for k, v in topics.items():
	topic_data = requests.get(v['url']).json()
	for material in topic_data['materials']:
		materials[material['url'][1:]] = material

eu_api = requests.get('https://usegalaxy.eu/api/tools?in_panel=False').json()
au_api = requests.get('https://usegalaxy.org.au/api/tools?in_panel=False').json()
us_api = requests.get('https://usegalaxy.org/api/tools?in_panel=False').json()
be_api = requests.get('https://usegalaxy.be/api/tools?in_panel=False').json()
fr_api = requests.get('https://usegalaxy.fr/api/tools?in_panel=False').json()

eu_tools = [x['id'] for x in eu_api]
au_tools = [x['id'] for x in au_api]
us_tools = [x['id'] for x in us_api]
fr_tools = [x['id'] for x in fr_api]
be_tools = [x['id'] for x in be_api]


def find_tool(tool, server):
	tool = tool.replace('%2F', '/')
	if tool in server:
		return ""
	else:
		# We won't ask people to install these
		if 'interactive_tool' in tool:
			return ""

		# This is for sure there
		if tool == 'upload1':
			return ""

		if '/' not in tool:
			return f"# Our Error, {tool} is missing"
		else:
			# Version mismatch?
			possible = sorted([x.split('/')[5] for x in server if '/' in x and '/'.join(tool.split('/')[0:5]) == '/'.join(x.split('/')[0:5])])[::-1]

			tool = tool.replace('%20', ' ')
			if tool not in guid:
				# 2.6+galaxy0 is not an installable revision.
				if tool == 'toolshed.g2.bx.psu.edu/repos/bgruening/flye/flye/2.6+galaxy0':
					tool = 'toolshed.g2.bx.psu.edu/repos/bgruening/flye/flye/2.6'
				# Not sure why/how.
				elif tool == 'toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/datamash_ops/1.0.6':
					tool = 'toolshed.g2.bx.psu.edu/repos/iuc/datamash_ops/datamash_ops/1.0.6'
				else:
					raise Exception(f"We cannot handle {tool}")

			data = guid[tool]
			# ['lparsons', 'cutadapt', '660cffd8d92a']
			if len(possible) == 0:
				return "\n".join([
					f"- name: {data[1]}",
					f"  owner: {data[0]}",
					f"  revisions: [{data[2]}]",
					f"  tool_panel_section_label: Smörgåsbord Tools",
					f"  tool_shed_url: https://toolshed.g2.bx.psu.edu/",
					""
				])
			else:
				tool_version = tool.split('/')[5]
				return "\n".join([
					f"- name: {data[1]} # We observed versions {', '.join(possible)} but the training is tested with version {tool_version}",
					f"  owner: {data[0]}",
					f"  revisions: [{data[2]}]",
					f"  tool_panel_section_label: Smörgåsbord Tools",
					f"  tool_shed_url: https://toolshed.g2.bx.psu.edu/",
					""
				])
			#print(tool, possible)
			#return tool, possible


def fmt_yml(tools, mod, title):
	if len(tools) > 0:
		return f"# {mod} / {title}\n" + '\n'.join(tools)
	else:
		return f"# {mod} / {title}\n"


def determine_support(module, video):
	has_workflows = False
	has_wf_tests = False

	if 'Tutorial' not in video.get('type', 'noen'):
		return
	
	if module == 'Galaxy Admin Training':
		return

	eu_supports = []
	au_supports = []
	us_supports = []
	fr_supports = []
	be_supports = []
	for mat in [x for x in v['materials'] if x.get('type', 'none') == 'Tutorial']:
		print(mat)
		tools = materials[mat['link']]['tools']
		for tool in list(set(tools)):
			print("\t", tool)
			eu_supports.append(find_tool(tool, eu_tools))
			au_supports.append(find_tool(tool, au_tools))
			us_supports.append(find_tool(tool, us_tools))
			fr_supports.append(find_tool(tool, fr_tools))
			be_supports.append(find_tool(tool, be_tools))

		wfs = materials[mat['link']].get('workflows', [])
		if len(wfs) > 0:
			has_workflows = True
		if any([x['tests'] for x in wfs]):
			has_wf_tests = True

	return {
		'eu': fmt_yml([x for x in eu_supports if x != ""], module, video['title']),
		'au': fmt_yml([x for x in au_supports if x != ""], module, video['title']),
		'us': fmt_yml([x for x in us_supports if x != ""], module, video['title']),
		'fr': fmt_yml([x for x in fr_supports if x != ""], module, video['title']),
		'be': fmt_yml([x for x in be_supports if x != ""], module, video['title']),
	}

for k in ('eu', 'au', 'us', 'fr', 'be'):
	with open(f'ask_{k}.txt', 'w') as handle:
		handle.write("""
---
install_tool_dependencies: true
install_repository_dependencies: true
install_resolver_dependencies: true

# Below is a list per tutorial, please feel free to skip installing tools you
# do not want to support.
#
# This is completely voluntary!
#
# For tools where we know a similar version is in your Galaxy we have provided a list
# Please check the list and decide if you want to support that version, or not.
tools:
""".lstrip())

def emit(module, session, v):
	q = determine_support(module, v)
	for k in ('eu', 'au', 'us', 'fr', 'be'):
		with open(f'ask_{k}.txt', 'a') as handle:
			try:
				handle.write(q[k])
			except:
				pass

has_emitted_row = {}
for module_id, module in modules.items():
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

				row = emit(
					module['title'],
					"",
					v
				)

			elif 'session' in item:
				sesh = sessions[item['session']]
				for vk in sesh['videos']:
					if vk in has_emitted_row:
						continue
					else:
						has_emitted_row[vk] = True

					v = videos[vk]
					row = emit(
						module['title'],
						sesh['title'],
						v
					)
			else:
				pass
