---
layout: default
---

{% for page in site.pages %}
  {% if page.layout == 'event' %}
   [{{page.title}}]({{site.baseurl}}{{page.url}})
  {% endif %}
{% endfor %}
