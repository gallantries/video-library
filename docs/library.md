---
layout: default
---

# Welcome to the Galaxy Training Video Library!

This page shows you the full library of available GTN video tutorials, you can use these for self-study, courses, and more! Below are all of the individual videos, but some videos are part of multi-video "sessions" which can be found in the [session library]({% link session-library.md %})

<div markdown="0">
{% include button.html link="/session-library" colour="yellow" label="Multi-Video Sessions" buttonsize="large" %}

{% include button.html link="/modules" colour="pink" label="Training Modules" buttonsize="large" %}

{% include button.html link="/instructors" colour="blue" label="Adding Videos" buttonsize="large" %}
</div>

<br>

## All Training Videos

Here is the full list of all individual training videos

<div class="accordion" id="accordionvideos">
{% for tag in site.data['by_tags'] %}
    {% assign tag-name = tag[0] | slugify %}
	<h3 style="text-transform:capitalize;" id="{{ tag-name }}">{{ tag[0] | replace: '-',' ' | capitalize }}</h3>
	{% for video in tag[1]['videos'] %}
		{% assign id=video[0] %}
		{% assign s=video[1] %}
		{% include session.html session=s id=id type="video" module=tag-name %}
	{% endfor %}
{% endfor %}
</div>
