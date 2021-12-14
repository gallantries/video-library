---
layout: default
---

# Galaxy Training Video Session Library

This page shows you only the multi-video "sessions" of available GTN video tutorials, you might also be interested in the [full video library]({% link library.md %}) which includes every single video known to the GTN Video Library.

<a href="library"><button type="button" class="btn btn-warning">All Videos</button></a>

## All Training Sessions

Sessions are multi-video trainings often taught as a unit, for example a lecture video and a hands-on video from the same GTN tutorial.

<div class="accordion" id="accordionsessions">
{% for tag in site.data.sessions_bytag %}
  {% assign tag-name = tag[0] | slugify %}
  <h3 style="text-transform:capitalize;" id="{{ tag-name }}">{{ tag[0] | replace: '-',' ' | capitalize }}</h3>
  {% for session in tag[1] %}
  {% assign id=session[0] %}
  {% assign s=session[1] %}
  {% include session.html session=s id=id type="session" module=tag-name %}
  {% endfor %}
{% endfor %}
</div>
