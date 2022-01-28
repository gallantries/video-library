---
layout: event
title: "My Awesome Event (Example)"
description: "Best training since sliced bread lessons"
location: "The North Pole"
instructors: [fpsom, shiltemann, bebatut, abretaud, yvanlebras, hexylena]
date:
  start: 2021-11-15
  end: 2021-11-18
registration: "https://example.com/registration"
cost: free
contacts: [shiltemann, hexylena]
example: true

setup:
  servers:
    - server: eu
      tiaas: smorg2021  # if using TiaaS for this server, but the keyword here
    - server: au
    - custom:
        name: My custom Galaxy server
        url: "https://galaxy.example.com"
  slack:
    event_channel:
      name: "#event-testevent"
      link: "https://gtnsmrgsbord.slack.com/archives/C01EDBVMHBQ"

certificates:
  - request_form: ""

wrapup:
  feedback_form: "https://feedback.example.com"


program:
  preliminary:
    title: Before you start
    trainings:
      - setup
      - video: community/welcome
  day1:
    title: Day 1
    description: your first intro
    trainings:
      - icebreaker:
          prompt: "Introduce yourself and tell us your favorite science fun fact!"
          channel_link: example  # defaults to the event channel if not set, and #social if no event channel set
          channel_name: "#mychannel"
          certificate: false  # set this if you would like to encourage participation in icebreakers in order to receive certificate
      - session: webinars
      - session: sequence-analysis/quality-control
  module2:
    title: Day 2
    description: deeper dive
    trainings:
      - session: webinars
        instructors: [hexylena, bebatut]
      - session: sequence-analysis/quality-control

---
