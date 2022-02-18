---
layout: module
title: SARS-CoV-2 Data Analysis

program:
  intro:
    title: "Introduction to Galaxy"
    trainings:
      - video: galaxy/intro
      - video: introduction/galaxy-intro-101/tutorial
      - video: introduction/galaxy-intro-ngs-data-managment
  day2:
    title: "Data Upload & Quality Control"
    trainings:
      - session: sequence-analysis/quality-control
      - session: sequence-analysis/mapping
      - video: galaxy-interface/collections/tutorial
      - self-study: sequence-analysis/human-reads-removal

  day3:
    title: "SARS-CoV-2 Data Analysis on Public Datasets"
    trainings:
      - video: sars-cov2/using-galaxy
      - video: variant-analysis/sars-cov-2-variant-discovery/tutorial
      - video: galaxy-interface/workflow-automation
      - video: sars-cov2/usegalaxy-star-bot

  day4:
    title: "Visualisation & Data Export"
    trainings:
      - external:
          title: Accelerating Research through data sharing
          video: "https://drive.google.com/file/d/12yPW6ku8KQeKFUYs9VBaDsP7ilaMk5XM/preview"
          length: 13m
          author: Carla Cummins
      - video: galaxy-interface/upload-to-ena
      - external:
          title: Upload data to a local datastore
          description: |
            So you’ve used Galaxy workflows to analyze your SARS-CoV-2 samples?
            Learn in this tutorial how to export results to your favorite datastore.
          video: -5U0sINjoig
          length: 10m
          author: Wolfgang Maier
      - external:
          title: Introduction to Viral Beacon
          description: |
            How to visualize tens of thousands of SARS-CoV-2 analysis results?
            Learn about the Viral Beacon project’s solution!
          video: R_4yUMPk7eY
          length: 25m
          slides: "https://drive.google.com/file/d/1yCHOi1EGKpkH-3XpKTKNKpFjwYAWKSVx/preview"
          author: Babita Singh
      - external:
          title: Using and Customising ObservableHQ
          description: |
            In this demo you will get to know the ObservableHQ platform for interactive data
            visualization. You will see how covid19.galaxyproject.org uses it to build a
            dashboard for their SARS-CoV-2 analysis efforts and will learn how to customize
            this solution to fit your own purposes.
          video: oeqPestqdAw
          length: 15m
          author: Sergei Pond

  extra:
    title: Optional Extra Training
    trainings:
      - session: galaxy-interface/ncbi-sarf
      - video: assembly/assembly-with-preprocessing
      - video: proteomics/pandemic/external
      - self-study: dev/bioblend-api
        type: slides
      - external:
          title: "Case Studies: What you can do with SARS-COV-2 data"
          description: Learn what you can do with SARS-CoV-2 data
          video: R4EoTEiAQNE
          length: 37m
          author: Andrew Page


---

This module covers the contents of the <a href="https://galaxyproject.eu/event/2021-06-21-sars-cov-2-data-analysis-monitoring-training/">SARS-CoV-2 with Galaxy course</a>, first run in August 2021

