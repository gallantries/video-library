---
layout: course-handbook
---

# Welcome to the Galaxy Training Video Library!

This page shows you the full library of available GTN video tutorials, you can use these for self-study,

<div class="accordion" id="accordionall">
{% for video in site.data.videos %}
  {% include session.html session=video module="all" %}
{% endfor %}
</div>
