---
layout: module
title: Galaxy Admin Training
description: Learn how to run a Galaxy server

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
      - video: admin/tus/tutorial
      - video: admin/singularity/tutorial
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
      - video: dev/tool-from-scratch/tutorial
      - video: admin/interactive-tools
      - video: admin/upgrading/tutorial
      - video: admin/object-store/exercise
      - self-study: admin/jenkins
        support_channel: event-gat
      - self-study: admin/ftp
      - self-study: admin/advanced-galaxy-customisation
      - self-study: admin/troubleshooting

---

