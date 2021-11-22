---
layout: default
title: "Statistics!"
---
<h1>Video Data</h1>
<div class="row">
	<div class="col-md-12">
	<div class="card bg-primary text-white">
		<div class="card-body">
			<h2 class="card-title" style="font-weight: 900; font-size: 300%">{{ site.data.stats._total_ | round:1 }}</h2>
			<p class="card-subtitle mb-2">hours</p>
			<p class="card-text">Of video content in the GTN & Gallantries' Video Library</p>
		</div>
	</div>
	</div>
</div>

<div class="row">
	{% for tag in site.data.stats.bytag %}
	<div class="col-md-3">
		<div class="card">
		<div class="card-body">
			<h2 class="card-title">{{ tag[1] | round:1 }}</h2>
			<p class="card-subtitle mb-2 text-muted">hours</p>
			<p class="card-text">of {{ tag[0] }} videos</p>
		</div>
		</div>
	</div>
	{% endfor %}
</div>

<h1>Speaker Data</h1>

<table>
	<thead>
		<tr>
			<th>Speaker</th>
			<th>Duration (hours)</th>
		</tr>
	</thead>
	<tbody>
	{% for speaker in site.data.stats.byspeaker %}
		<tr>
			{% assign x = speaker[0] %}
			<td>{{ site.data.instructors[x].name | default: x}}</td>
			<td>{{ speaker[1] | round: 1 }}</td>
		</tr>
	{% endfor %}
	</tbody>
</table>

<h1>Captioner Data</h1>
<table>
	<thead>
		<tr>
			<th>Contributor</th>
			<th>Hours of Captions Reviewed</th>
		</tr>
	</thead>
	<tbody>
	{% for captor in site.data.stats.bycaptioner %}
		{% if captor[0] %}
		<tr>
			{% assign x = captor[0] %}
			<td>{{ site.data.instructors[x].name | default: x}}</td>
			<td>{{ captor[1] | round: 1 }}</td>
		</tr>
		{% endif %}
	{% endfor %}
	</tbody>
</table>
