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
 {% for page in site.pages %}
  {% if page.layout == 'event' %}
  <tr>
   <td> <a href="{% if page.external %}{{page.external.link}}{% else %}{{site.baseurl}}/{{page.url}}{%endif%}"> {{page.title}} </a> </td>
   <td> {% include dates.html start=page.date.start end=page.date.end %} </td>
  </tr>
  {% endif %}
 {% endfor %}
 </tbody>
</table>
