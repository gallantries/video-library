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
   <td> <a href="{{site.baseurl}}{{page.url}}"> {{page.title}} </a> </td>
   <td> {{ page.date.start | date: "%-d %B %Y" }} </td>
  </tr>
  {% endif %}
 {% endfor %}
 </tbody>
</table>
