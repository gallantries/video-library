---
layout: default
---

<table class="table-striped">
 <thead>
  <tr>
   <th> Event Name </th>
   <th> When </th>
  </tr>
 </thead>
 <tbody>
 {% assign sortedpages = site.pages | sort: "date" | reverse %}
 {% for page in sortedpages %}
  {% if page.layout == 'event' %}
  <tr>
   <td> <a href="{% if page.external %}{{page.external.link}}{% else %}{{site.baseurl}}{{page.url}}{%endif%}"> {{page.title}} </a> </td>
   <td> {% include dates.html start=page.date.start end=page.date.end %} </td>
  </tr>
  {% endif %}
 {% endfor %}
 </tbody>
</table>
