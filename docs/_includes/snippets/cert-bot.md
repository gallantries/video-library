#### Using the GTN Certificate Slack Bot {% unless page.layout == 'default' %}<a href="{% link certbot.md %}">{% icon external-link %}{: style="height:0.5em;color: blue"}</a>{% endunless %}


- **Completed a tutorial?**
  1. **Share your Galaxy history** via URL
    - [Instructions](https://training.galaxyproject.org/training-material/faqs/galaxy/histories_sharing.html)
    - The history URL will look something like: `https://usegalaxy.xx/u/saskia/h/my-history-name`
  2. **Open the Slack channel for the tutorial** you finished
     - Link to this channel is listed below the video
  2. **Submit your history URL** to the bot  in this channel using the command:
    - /completed {% unless include.gat %}https://link_to_your_history{% endunless %}
  3. **Write a short message** in the channel letting us know what you thought of the tutorial, and/or thanking the instructors!
<br><br>
- **Want to check your submissions?**
  - At any time, use the /transcript command to see what you have already submitted
  - In **any channel**, or a message to [@GTN Certificate Bot](https://gtnsmrgsbord.slack.com/app_redirect?channel=U02EWBWKWKT)
<br><br>
- **Finished with the event?** Use the command:
  - /request-certificate <Your Full Name>
    - to request a certificate for the course.
    - Enter your name as you would like it to appear on the Certificate
  - In **any channel**, or a message to [@GTN Certificate Bot](https://gtnsmrgsbord.slack.com/app_redirect?channel=U02EWBWKWKT)
  {%- if include.config.deadline -%}- Deadline: {{include.config.deadline | date_to_long_string }}{% endif %}
  - We will review your Galaxy histories, and send you your personalised certificate
    - We aim to do this within 2 weeks of the certificate deadline

<video controls width="100%">
    <source src="{% link assets/images/certbot.mp4 %}"
            type="video/mp4">
    Sorry, your browser doesn't support embedded videos.
</video>
