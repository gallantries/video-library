---
layout: default
---

{% for page in site.pages %}
  {% if page.layout == 'event' %}
   [{{page.title}}]({{page.url}})
  {% endif %}
{% endfor %}
