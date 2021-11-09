---
layout: default
---

{% assign program = page.program | default: site.data.videos %}

{{ content }}


{% for session in program %}

{% endfor %}
