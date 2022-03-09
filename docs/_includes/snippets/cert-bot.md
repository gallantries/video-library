#### Using the GTN Certificate Bot {% unless page.layout == 'default' %}<a href="{% link certbot.md %}">{% icon external-link %}{: style="height:0.5em;color: blue"}</a>{% endunless %}


- **Completed a tutorial?**
  - **Share your Galaxy history** via URL ([instructions](https://training.galaxyproject.org/training-material/faqs/galaxy/histories_sharing.html))
    - The history URL will look something like: `https://usegalaxy.xx/u/saskia/h/my-history-name`
  - Submit your history URL to the bot using the command:
    - `/completed{% unless include.gat %} <link to your Galaxy History>{% endunless %}`
    - Do this in the **channel for the tutorial** you completed (linked below video)
  - **Write a short message** in the channel letting us know what you thought of the tutorial, and/or thanking the instructors!
<br><br>
- **Want to check your submissions?**
  - At any time, use the `/transcript` command to see what you have already submitted
  - In **any channel**, or a message to [@GTN Certificate Bot](https://gtnsmrgsbord.slack.com/app_redirect?channel=U02EWBWKWKT)
<br><br>
- **Finished with the event?**
  - Use the command `/request-certificate <Your Full Name>` to request a certificate for the course.
    - Enter your name as you would like it to appear on the Certificate
  - In **any channel**, or a message to [@GTN Certificate Bot](https://gtnsmrgsbord.slack.com/app_redirect?channel=U02EWBWKWKT)
  {%- if include.config.deadline -%}- Deadline: {{include.config.deadline | date_to_long_string }}{% endif %}
  - We will review your Galaxy histories, and send you your personalised certificate
    - We aim to do this within 2 weeks of the certificate deadline

