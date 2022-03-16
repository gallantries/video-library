---
layout: program
module: false
title: "Mycobacterium tuberculosis NGS made easy: data analysis step-by-step"
description: |
  ![banner](images/TBCAPT_NGS_Training_banner.jpg)

  Below you will find everything you need to follow this course! (Back to [Course Overview Page](./course.html))
  <br><br>

certbot: false
instructors: [dbrites,cstritt,andreacabibbe,annalenaguske, andreaspitaleri,GaloGS,arashghodousi,liliana-rutaihwa]

setup:
  servers:
    - server: eu
      tiaas: mtb-ngs

  slack:
    event_channel:
      name: "#event-mtb-ngs"
      link: "https://gtnsmrgsbord.slack.com/archives/C035Q01UA2F"

program:
  prelim:
    title: Welcome & Setup
    trainings:

      - external:
          title: Live Welcome session (optional)
          description: We would like to welcome you to this trainning, to present ourselves and to clarify any organizational question you might have.
          other:
            - label: Time
              value: 21st March, 10:30am-11:00am
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451

      - code-of-conduct
      - setup

  day1:
    title: "Day 1: Overview of NGS technologies & TB specific NGS solutions"
    description: |
      There were unusually high rates of TB cases in your country this year. To characterize the underlying
      bacterial factors driving the epidemic, isolates been sent for whole-genome sequencing.  Doctors and public
      health authorities request information in order to take decisions. In this course it will be demonstrated how
      you would make use of NGS to answer several questions relevant for patient and public health system management
      such as:
        - Are there cases of drug resistant bacteria?
        - Is there transmission of drug resistance?
        - Is there evidence of de novo emergence of resistance?
        - Are there multiple infections per patient?
        - Do we have on-going transmission?
        - Are there imported cases?
        - Can we say that we have ancestral strains infecting patients in our population?

      We hope that at the end of the different training sessions you can answer this question on your own!

    trainings:
      - icebreaker:
         - prompt: "Introduce yourself and tell us one fun fact about yourself!"
           channel: "event-mtb-ngs"
      - external:
          title: "Webinar: Overview of NGS technologies & TB specific NGS solutions"
          description: |
            This webinar will introduce different sequencing technologies and what applies best to what
            kind of problem.
          video: BcfBjCJRmUs
          length: 1h10m
          author: Andrea Cabibbe
          note: |
            **Finished watching the webinar as part of the Mtb NGS event?** Share your thoughts with us [here](https://docs.google.com/document/d/1EfgttagZ8hBfjQiRznsCgDYVpzi3CF55cHqjarYa97o/edit#heading=h.e69aqv1nq3gw)

            *The completion of this assessment is a requirement for the certificate of attendance.*
      - external:
          title: "Webinar: Implementation of NGS for TB- WHO documents and other considerations"
          author: Andrea Cabibbe
          video: eSWnPange8w
          description: |
            This webinar will summarize the recommendations and considerations available from the WHO
            documents on the use of NGS for TB
          length: 1h
          note: |
            **Finished watching the webinar as part of the Mtb NGS training event?** Share your thoughts with us [here](https://docs.google.com/document/d/1yCSyBnC1D5-czrW8xUi8sS2ffk_igB7quqhbHr7PE-U/edit#)

            *The completion of this assessment is a requirement for the certificate of attendance.*
      - external:
          title: Q&A session
          description: |
            If you are part of the Mtb NGS training event we would like to hear your opinion on the following questions and promote discussion in this Q&A session. Please let us know your thoughts on one or more of the following questions in the shared notes; 1) How do I choose the right sequencing technology for my samples? 2) What is needed for NGS? 3) Why is NGS better for drug resistance and outbreak analysis? Also take the chance to ask us or write down in the shared notes other questions you might have.

            *The completion of this assessment is a requirement for the certificate of attendance.*
          other:
            - label: Time
              value: "14:00 -16:00 CET"
            - label: Shared notes
              link: https://docs.google.com/document/d/1VtGho4Zz0qFp5tzqD8rl7NU83xtYb4tCkLDitC3DrhQ/edit#
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451


  day2:
    title: Mapping and Variant calling in MTBC
    description: |
      The 20 strains isolated in your country have been sequenced with Illumina technology
      to obtain whole-genome sequences. In this part of the workshop you will learn how to
      analyse those sequences.

      In a typical bioinformatic pipeline you would store your sequences in a computer server
      where all necessary software would be installed. This would be a server running the
      operating system LINUX, which is the most efficient way to run bioinformatics pipelines
      (more on this on Day 4). You will be running your analysis in a LINUX server from Galaxy,
      but instead of writing directly commands to execute operations in the server, you will be
      executing operations through a Galaxy graphical interface. This allows you to have access
      to a LINUX server and to run workflows without knowing LINUX. Importantly, for training
      purposes  it also allows you to dedicate more attention in trying to understand what is
      being done in each of the steps without having to understand the programing behind. This
      being said, working directly on a LINUX cluster provides you always more flexibility, but
      if you don’t have access to one, Galaxy is a very good alternative for data analysis.

      You will need to understand how to use Galaxy to run all the hands-on tutorials and
      therefore is highly recommended that you follow the next webinar and hands-on on Galaxy.
      The good thing about this is that once you know how it works, you can use it to run your
      own analysis with your own data.
    trainings:
      - icebreaker:
        - prompt: "What is the coolest, most mind blowing fact (nature/people/animal etc.) you know?"
          channel: event-mtb-ngs

  day2-1:
    title: "Session 1: Learning Galaxy"
    subday: true
    trainings:
      - video: galaxy/intro
      - video: introduction/galaxy-intro-101/tutorial

  day2-2:
    title: "Session 2: Mapping and Variant calling of short MTBC reads"
    subday: true
    description: |
      Once you have received your sequences, the first step is to assess the quality of
      sequencing. Once we are sure that the sequencing worked well, we typically compare our
      sequencing results to a reference genome (re-sequencing approach) by using a
      bioinformatics procedure usually called mapping. After, we will identify the genomic
      variants in our sequences with respect to the reference genome, a bioinformatics procedure
      called, variant calling. Once we are certain of the variants we have identified, usually
      we are interested in determining to what genes they belong, to what pathways or for
      instance if they are likely to disrupt protein function. This procedure is called
      annotation. Once we have gone through each of these steps we are ready to analyse drug
      resistant patterns, draw phylogenetic relationships or identify recent transmission of M.
      tuberculosis.

      You are now ready for performing bioinformatic analysis in Galaxy. Before we start we
      would like you to watch a short video on how Illumina sequencing works. Following that
      video we have prepared a webinar on mapping and variant calling of Illumina applied to
      MTBC. After watching it you will be hopefully able to know; how a reference genome is
      chosen, why we typically ignore some regions of the MTBC genomes or what is the difference
      between a fixed and a variable SNP and why do we care about it (among other things).


    trainings:
      - external:
          title: Illumina sequencing principle video
          video: fCd6B5HRaZ8
          length: 5m
      - external:
          title: "Webinar: Mapping and Variant calling"
          description: Main bioinformatics steps involved in mapping and variant calling from Illumina short reads applied to MTBC
          video: todo
          length: 45m
          video: 38GUBKwWXv8
          author: Daniela Brites
          note: |
            **Finished watching the webinar as part of the Mtb NGS training event?** Share your thoughts with us [here](https://docs.google.com/document/d/18y0PScnbA0GuLKjITzIr01wyLVWH6RYPAE5RWkwlfNA/edit#heading=h.bs9dcv9mioqd)

            *The completion of this assessment is a requirement for the certificate of attendance.*

      - external:
          title: Q&A session
          description: Meet the the experts
          author: Daniela Brites & Galo A. Goig
          other:
            - label: Time
              value: "11:30-12:30 CET"
            - label: Zoom Link
              link: https://swisstph.zoom.us/j/84656236451
      - session: variant-analysis/tb-variant-analysis
      - external:
          title: Q&A session
          description: Meet the the experts
          author: Daniela Brites & Galo A. Goig
          other:
            - label: Time
              value: "16:30-17:30 CET"
            - label: Zoom Link
              link: https://swisstph.zoom.us/j/84656236451

  day3:
    title: "Day 3: Evolutionary epidemiology: using phylogenetics to understand DR emergence and Mtb transmission"
    description: |
      We are ready to analyse drug resistant patterns, draw phylogenetic relationships or
      identify recent transmission among the isolates we have sampled in our population. Before
      delving into the analysis of the genomes we would like to share with you some notions
      important to the inference of direct transmission and to the interpretation of drug
      resistant patterns.
    trainings:
      - icebreaker:
        - prompt: "What is your favorite dish (food or drink)? Bonus points for recipes!"
          channel: event-mtb-ngs
      - external:
          title: "Webinar: Drug resistance prediction"
          author: Galo A. Goig
          description: Principles of drug resistance detection from genomic data
          length: 20m
          video: Ddwt-_gQR2M
          note: |
            **Finished watching the webinar as part of the Mtb NGS training event?** Share your thoughts with us [here](https://docs.google.com/document/d/1WnvgYtTUOJGxTUEQCL0-HOlHNkqo293LaqaGB9EKojM/edit#heading=h.bs9dcv9mioqd)

            *The completion of this assessment is a requirement for the certificate of attendance.*

      - external:
          title: "Webinar: Phylogenetic and mutations"
          author: Galo A. Goig
          description: |
            This video will introduce two types of mutations to take into account when studying
            drug resistance patterns
          length: 15m
          video: 1ps_o5rpnmw
          note: |
            **Finished watching as part of the Mtb NGS training event?** Share your thoughts with us [here](https://docs.google.com/document/d/1I341zrHJdAn5BEtrtc1KmJZ_x_lez_EWA75iTFBq-R4/edit#)

            *The completion of this assessment is a requirement for the certificate of attendance.*
      - external:
          title: "Webinar: The concept of clustering"
          author: Galo A. Goig
          description: Main aspects of clustering analysis to infer transmission in MTBC
          length: 15m
          video: l4cPUECJ7VU
      - external:
          title: "Webinar: Genetic distance thresholds"
          author: Galo A. Goig
          description: Clustering as an approximation to infer transmission
          length: 15m
          video: kKNgmpy1N94
          note: |
            **Finished watching as part of the Mtb NGS training event?** Share your thoughts with us [here](https://docs.google.com/document/d/1Q4mw-y3FZrGvmz3VNQrLkLslsi5QoTgDxwhAYYYdvjI/edit#)

            *The completion of this assessment is a requirement for the certificate of attendance.*
      - external:
          title: "Hands-on: Performing clustering analysis & drug resistance prediction"
          author: Galo A. Goig
          description: Learning how to do clustering analysis and interpret drug resistance patterns
          length: 2h
          hands-on: https://training.galaxyproject.org/training-material/topics/evolution/tutorials/mtb_transmission/tutorial.html
      - external:
          title: Q&A
          description: Discussion with the experts
          author: Galo A. Goig & Christoph Stritt
          other:
            - label: Time
              value: "11:30-12:30 CET"
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451

      - external:
          title: "Hands-on: Inference of phylogenetic trees"
          description: Main principles of phylogenetic inference, tree interpretation
          author: Christoph Stritt
          length: 1h
          hands-on: https://training.galaxyproject.org/training-material/topics/evolution/tutorials/mtb_phylogeny/tutorial.html
      - external:
          title: Q&A
          author: Galo A. Goig & Christoph Stritt
          description: Discussion with the experts
          other:
            - label: Time
              value: "16:30-17:30 CET"
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451

  day4:
    title: Day 4

  day4-1:
    title: "Session 1: Webtools dedicated to MTBC bioinformatics"
    subday: true
    description: |
      The use of whole-genome sequencing (WGS) for antibiotic resistance prediction and routine
      typing of bacterial isolates has increased substantially in recent years. To date a
      multitude of solutions for analyzing WGS data of the Mycobacterium tuberculosis complex
      (MTBC) data have been developed. In the first part of the 4th day of this workshop, we
      introduce some freely available webtools and open source pipelines designed to analyze
      MTBC sequence data and we’ll provide some examples of how these tools work and how to
      interpret the results.
    trainings:
      - icebreaker:
        - prompt: "What is a book, film, tv show or game that you've enjoyed recently?"
          channel: event-mtb-ngs
      - external:
          title: "Webinar: Web tools for analysis of MTBC sequenced data"
          author: Arash Ghodousi
          description: Introduction to most common web tools for fast identification of bacterial species from raw sequencing reads
          length: 50m
          video: HVQaq2GXCAc
          note: |
            **Finished watching as part of the Mtb NGS training event?** Share your thoughts with us [here](https://docs.google.com/document/d/1jdp61AFeyd_fK8XWZ348k7aok779feiCQ3q2uz1RPF0/edit#)

            *The completion of this assessment is a requirement for the certificate of attendance.*
      - external:
          title: "Webinar: Introduction to the MTBseq pipeline"
          author: Arash Ghodousi
          description: Introduction to MTBseq pipeline, an automated pipeline for mapping, variant calling and detection of resistance mediating and phylogenetic variants from whole genome sequence data of MTBC
          length: 30m
          video: ob29WYXwLxo

      - external:
          title: Q&A
          description: Meet the the experts
          author: Andrea Spitaleri
          other:
            - label: Time
              value: "11:30-12:30 CET"
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451

  day4-2:
    title: "Session 2: Be a bioinformatician in the jungle (optional)"
    subday: true
    description: |
      On Day 2 and 3 you have learned how you could use galaxy for analysing your own data.
      Establishing your own workflows in galaxy would allow you combining different tools and
      build your own pipeline without having to know how to program. If you are not so
      interested in having your own pipeline, webtools for WGS analysis can be very useful, as
      we have shown in the previous session.

      However, in the last part of the training we would like to convey to you what it would
      take if would want to run Linux via the command line.  The Linux operating system will be
      introduced, how to perform basic tasks using the Unix shell and how to install and run
      pipelines on the command line. You will learn the power of the Unix shell in performing
      complex and powerful tasks, often with just a few keystrokes or lines of code. In fact,
      Unix shell helps users automate repetitive tasks and easily combine smaller tasks into
      larger, more powerful workflows (i.e. pipelines). Use of the shell is fundamental to a
      wide range of advanced computing tasks, including high-performance computing. These
      webinars will introduce you to this powerful tool. Which approach to choose, Galaxy
      workflows, Webtools or native Linux depends on your needs, your interests and what
      computer resources you have available.

    trainings:
      - external:
          title: "Webinar: Introduction to Linux"
          author: Andrea Spitaleri
          description: "Introduction to Linux OS: installation and usage"
          length: 35m
          video: N8rW07ByQOE
      - external:
          title: "Webinar: How to run programs (Python, Docker, Singularity)"
          author: Andrea Spitaleri
          description: Learning how to install and use programs to analyze data
          length: 35m
          video: feYweAQNGS8
      - external:
          title: "Webinar: Demo on how to run the Linux command line"
          author: Andrea Spitaleri
          description:   Demo video on how to use the shell commands
          length: 20m
          video: 7V7LCjUEg1c
      - external:
          title: "Hands-on: The Unix Shell"
          author: The Carpentries
          description: Recommended tutorial from software carpentries to those wanting to learn Linux.
          length: 4h
          tutorial: "https://swcarpentry.github.io/shell-novice/"
      - external:
          title: Q&A
          description: Discussion with the experts
          author: Arash Ghodousi & Andrea Spitaleri
          other:
            - label: Time
              value: "16:30-17:30 CET"
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451

  day5:
    title: Day 5
    description: |
      Today all experts will  be available to answer your questions and discuss any
      of the tutorials, webinars or questions related to your own data. Meet with us at the
      zoom link!
    trainings:
      - external:
          title: Q&A
          description: Discussion with the experts
          author: All
          other:
            - label: Time
              value: "10:00-12:30 CET"
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451

---
