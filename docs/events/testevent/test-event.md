---
layout: event
id: test
title: "My Awesome Event (Example)"
description: "Best training since sliced bread lessons"
location: "The North Pole"
format: Asynchronous with some live Q&A sessions
instructors: [fpsom, shiltemann, bebatut, abretaud, yvanlebras, hexylena]
institutions: [gtn, gallantries]  # refer to institutes in affiliations.yaml, these will be listed as organisers and in the acknowledgement section of the page

date:
  start: 2021-11-15
  end: 2021-11-18
registration: "https://example.com/registration"
cost: free
contacts: [shiltemann, hexylena]

practical:  # anything else you want to list in the practical session can go here
  - name: My custom Info
    text: Anything else you want to list in practical info section
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
      useforall: true  # set this if you want all questions to go here, rather than the individual tutorial channels

certificates:  # optional. If you provide certificates for your event, which participants should request
  request_form: "https://feedbackform.example.com"
  deadline: 2022-07-24
  notes:  # if you want to provide more explanation here, either specificy "notes: my text about certs" or reuse an available snippet as shown below
    snippet: "snippets/cert-requirements-smorg.html"

feedback:  # optional. If you have a feedback survey for your course
  form: "https://feedback.example.com"


program:
  preliminary:   # you can define various sections (e.g. days) here
    title: Before you start
    trainings:
      - setup
      - code-of-conduct
      - certificates               # a predefined "session" explaining about certificates
      - video: community/welcome   # this points to a video in our video library
  day1:
    title: Day 1
    description: your first intro
    trainings:
      - icebreaker:
          - prompt: "Introduce yourself and tell us your favorite science fun fact!"
            channel: "mychannel"
            certificate: false  # set this if you would like to encourage participation in icebreakers in order to receive certificate
      - session: webinars          # sessions are multi-video tutorials (e.g. lecture & hands-on), see our session library for these
      - session: sequence-analysis/quality-control
  module2:
    title: Day 2
    description: deeper dive
    trainings:
      - session: webinars
        instructors: [hexylena, bebatut]
      - session: sequence-analysis/quality-control
      - self-study: climate/fates   # you can also add GTN tutorials that don't have videos, format is <topics>/<tutorial id> (find this in the GTN url of the tutorial)
        type: [slides, tutorial]    # does thit tutorial have slides, tutorial or both?
      - self-study: climate/fates
        type: [slides]
      - self-study: assembly/mrsa-nanopore  # default type is tutorial only
        description: This tutorial will cover X  # add a description
        prefix: "Hands-on: "                     # prefix for the session title
      - external:                   # if you want to include something outside of the GTN? No problem!
          title: My External Session
          description: This is a training that is not in the GTN, but it will teach you about XYZ
          video: oAVjF_7ensg  # a youtube id, or a video embed link
          length: 1h35m
          slides: "https://galaxyproject.org/"
          tutorial: "https://galaxyproject.org/"
          other:    # Any other info you want to apear in the table
            - label: Home Page
              link: "https://galaxyproject.org/"
            - label: Time
              value: "11:30-12:30 CET"
          author: "External Person X"



  wrapup:
    title: Wrap-up
    description: Thanks for joining this course!
    trainings:
      - feedback        # predifind section, this will link to the survey form you defined above.
      - certificates
---
