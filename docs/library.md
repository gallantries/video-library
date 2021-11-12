---
layout: course-handbook
---

# Welcome to the Galaxy Training Video Library!

This page shows you the full library of available GTN video tutorials, you can use these for self-study,

## All Training Sessions

Sessions are multi-video trainings often taught as a unit, for example a lecture video and a hands-on video from the same GTN tutorial.

<div class="accordion" id="accordionsessions">
{% for session in site.data.sessions %}
  {% assign id=session[0] %}
  {% assign s=session[1] %}
  {% include session.html session=s id=id type="session" module="sessions" %}
{% endfor %}
</div>

## All Training Videos

Here is the full list of all individual training videos

<div class="accordion" id="accordionvideos">
{% for tag in site.data['by_tags'] %}
	<h3 id="{{ tag[0] | slugify }}">{{ tag[0] }}</h3>
	{% for video in tag[1]['videos'] %}
		{% assign id=video[0] %}
		{% assign s=video[1] %}
		{% include session.html session=s id=id type="video" module="videos" %}
	{% endfor %}
{% endfor %}
</div>
