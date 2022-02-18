---
layout: event
id: test
title: "My Awesome Event (Example)"
description: "Best training since sliced bread lessons"
location: "The North Pole"
format: Asynchronous with some live Q&A sessions
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
    - server: eu        # some popular servers are predefined (in _data/servers.yml)
      tiaas: smorg2021  # if using TiaaS for this server, put the keyword here
    - server: au
    - custom:           # or you can specify a different server
        name: My custom Galaxy server
        url: "https://galaxy.example.com"
  slack:
    event_channel:
      name: "#event-testevent"
      link: "https://gtnsmrgsbord.slack.com/archives/C01EDBVMHBQ"

certificates:
  request_form: "https://feedbackform.example.com"
  deadline: 2022-07-24
  notes:  # if you want to provide more explanation here, either specificy "notes: my text about certs" or reuse an available snippet as shown below
    snippet: "snippets/cert-requirements-smorg.html"

feedback:
  form: "https://feedback.example.com"


program:
  preliminary:
    title: Before you start
    trainings:
      - setup
      - code-of-conduct
      - certificates
      - video: community/welcome
  day1:
    title: Day 1
    description: your first intro
    trainings:
      - icebreaker:
          - prompt: "Introduce yourself and tell us your favorite science fun fact!"
            channel: "mychannel"
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
      - self-study: climate/fates
        type: [slides, tutorial]
      - self-study: climate/fates
        type: [slides]
      - self-study: assembly/mrsa-nanopore  # default type is tutorial only
      - external:
          title: My External Session
          description: This is a training that is not in the GTN, but it will teach you about XYZ
          video: oAVjF_7ensg  # a youtube id, or a video embed link
          slides: "https://galaxyproject.org/"
          tutorial: "https://galaxyproject.org/"
          other: "https://galaxyproject.org/"
          author: "External Person X"



  wrapup:
    title: Wrap-up
    description: Thanks for joining this course!
    trainings:
      - feedback
      - certificates
---
