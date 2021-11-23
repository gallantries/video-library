---
layout: course-handbook
---

# Galaxy Training Video Session Library

This page shows you only the multi-video "sessions" of available GTN video tutorials, you might also be interested in the [full video library]({% link library.md %}) which includes every single video known to the GTN Video Library.

## All Training Sessions

Sessions are multi-video trainings often taught as a unit, for example a lecture video and a hands-on video from the same GTN tutorial.

<div class="accordion" id="accordionsessions">
{% for session in site.data.sessions %}
  {% assign id=session[0] %}
  {% assign s=session[1] %}
  {% include session.html session=s id=id type="session" module="sessions" %}
{% endfor %}
</div>
