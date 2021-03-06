---
layout: event
id: 'gcc2022-gtd-gat'
title: "Admin Training @ GCC 2022: Online Training Day"
status: final
description: "Free, global, training day ahead of the Galaxy Community Conference 2022. This day is meant to get you up to speed with the basics, so that you can get the most out of the training sessions at the GCC2022 conference!"
location: Online
instructors: [hexylena, natefoo, slugger70]
date:
  start: 2022-07-08
  end: 2022-07-08
registration: "https://galaxyproject.org/events/gcc2022/"
cost: Free
format: Asynchronous (no live sessions, pre-recorded videos, support via Slack, YOU decide your schedule)
contacts: [hexylena, shiltemann]
institutions: [jetstream2, gallantries, erasmusmc, elixir, gtn]

setup:
  slack:
    event_channel:
      name: event-gat
  servers:
  - disabled: true

program:
  setup:
    title: Welcome & Setup (Start Here!)
    description: Practical information about this course and getting everything set up to follow this course.
    trainings:
    - basics: logistics
    - basics: setup
    - basics: code-of-conduct
    - icebreaker:
      - prompt: Introduce yourself and tell us one fun fact about yourself!
        title: "Icebreaker"
        channel: event-gat

---

<p><strong>Attending the Admin Training session at GCC?</strong> Do you run a Galaxy server or would you like to learn how to do so? This module will help you get up to speed with everything you need to know to get the most out of the Admin Training sessions at the conference. </p>

{% include module_button.html link="gcc2022/gat-intro" colour="purple" label="Admin Training Basics" buttonsize="large" %}
