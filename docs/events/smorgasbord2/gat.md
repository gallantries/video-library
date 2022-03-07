---
layout: event
id: 'tapas-gat'
title: "Galaxy Admin Training @ GTN Tapas"
status: draft # draft, final (default)
description: "Free, Global, Online Week of Galaxy Admin Training"
location: Online
instructors: [hexylena, natefoo, slugger70, nsoranzo, mvdbeek, cat-bro]
date:
  start: 2022-03-14
  end: 2022-03-18
registration: "https://docs.google.com/forms/d/e/1FAIpQLSeoBxpkddbCXQps6p71lWit09Tt3qBQ1ewWraz4k0XmaX4_yg/viewform?usp=sf_link"
cost: free
contacts: [hexylena]

program:
  galaxyintro:
    title: Introduction to Galaxy
    description: "Start here if you are new to Galaxy. These videos will introduce you to the Galaxy platform, and walk you through your first analyses"
    trainings:
      - video: galaxy/intro
      - video: introduction/galaxy-intro-101-everyone/tutorial

  day1:
    title: Monday
    description:
    trainings:
      - session: admin/ansible
      - video: admin/ansible-galaxy/tutorial

  day2:
    title: Tuesday
    description:
    trainings:
      - video: admin/singularity/tutorial
      # TODO: TUS
      - session: admin/tool-management
      - video: admin/users-groups-quotas/slides
      - session: admin/cvmfs
      - video: admin/data-library/tutorial

  day3:
    title: Wednesday
    description:
    trainings:
      - video: admin/connect-to-compute-cluster/combined
      - video: admin/job-destinations/tutorial

  day4:
    title: Thursday
    description:
    trainings:
      - session: admin/pulsar
      - video: admin/gxadmin/slides
      - session: admin/monitoring
      - video: admin/maintenance/slides

  day5:
    title: Choose Your Own Adventure
    description:
    trainings:
      - video: community/welcome
      - video: admin/interactive-tools
      - video: admin/upgrading/tutorial
      - video: admin/object-store/exercise
      - self-study: admin/jenkins
      - self-study: admin/ftp
      - self-study: admin/advanced-galaxy-customisation
      - self-study: admin/troubleshooting

---

