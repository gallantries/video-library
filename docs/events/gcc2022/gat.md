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

  galaxyintro:
    title: Introduction to Galaxy
    description: "Start here if you are new to Galaxy. These videos will introduce you to the Galaxy platform, and walk you through your first analyses"
    trainings:
      - video: galaxy/intro
      - video: introduction/galaxy-intro-101-everyone/tutorial

  day1:
    title: Admin Training Basics
    description:
    trainings:
      - session: admin/ansible
      - video: admin/ansible-galaxy/tutorial

---

