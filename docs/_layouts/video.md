---
layout: default
---


{% assign v=site.data.videos[page.video] %}

<h3> GTN Video Library </h3>

{% include video-session.html vsession=v video=v.versions %}
