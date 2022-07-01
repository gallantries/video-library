---
layout: program
module: false
status: final
title: "Mycobacterium tuberculosis NGS made easy: data analysis step-by-step"
description: |
  ![banner](images/TBCAPT_NGS_Training_banner.jpg)

  - Back to [Course Overview Page](./course.html)
  - [YouTube Playlist](https://www.youtube.com/channel/UCVE9hc3WYKce2LPP1xQJuzg)

  Below you will find everything you need to follow this course!

  <br>

certbot: false
instructors: [dbrites, cstritt, andreacabibbe, annalenaguske, andreaspitaleri, GaloGS, arashghodousi, liliana-rutaihwa, pvanheus]

setup:
  servers:
    - server: eu
      tiaas: mtuberculosisngs

  slack:
    event_channel:
      name: event-mtb-ngs
      link: "https://gtnsmrgsbord.slack.com/archives/C035Q01UA2F"
      useforall: true
    notes: |
      **Be active on Slack!**
        - Join the Slack channel every day
        - Talk about the session you just attended! Got stuck? Have a question about the science? Want to discuss anything? Want to thank your instructors? Do it in Slack!
        - Enjoyed a hands-on tutorial? Take a moment to thank your (volunteer) instructors and speakers on Slack
        - And please, feel free to help other participants on Slack if you know the answer!"

certificates:
  request_form: "https://forms.gle/X2qgMQeobygH4orB8"
  certbot: false
  deadline: 2022-04-01

feedback:
  form: "https://forms.gle/6Xn8WudBvr3NMC3W7"

program:
  prelim:
    title: Welcome & Setup
    trainings:
      - setup
      - external:
          title: Live Welcome session (optional)
          description: We would like to welcome you to this trainning, to present ourselves and to clarify any organizational question you might have.
          other:
            - label: Time
              value: 21st March, 10:30am-11:00am
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451
      - code-of-conduct

  day1:
    title: "Day 1"
    description: |
      "There were unusually high rates of TB cases in your country this year. To characterize the underlying
      bacterial factors driving the epidemic, isolates have been sent for whole-genome sequencing.  Doctors and public
      health authorities request information in order to take decisions. In this course it will be demonstrated how
      you would make use of NGS to answer several questions relevant for patient and public health system management
      such as:
        - Are there cases of drug resistant bacteria?
        - Is there transmission of drug resistance?
        - Is there evidence of de novo emergence of resistance?
        - Are there multiple infections per patient?
        - Do we have on-going transmission?

      We hope that at the end of the different training sessions you can answer this question on your own!"

  day1-1:
    title: "Overview of NGS technologies & TB specific NGS solutions"
    subday: true

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
          author: andreacabibbe
          other:
            - label: Assessment
              value: "Finished watching the webinar as part of the Mtb NGS training event? Share your thoughts with us [here](https://docs.google.com/document/d/1EfgttagZ8hBfjQiRznsCgDYVpzi3CF55cHqjarYa97o/edit#heading=h.e69aqv1nq3gw)"
          note: |
            *The completion of this assessment is a requirement for the certificate of attendance.*
      - external:
          title: "Webinar: Implementation of NGS for TB- WHO documents and other considerations"
          author: andreacabibbe
          video: eSWnPange8w
          description: |
            This webinar will summarize the recommendations and considerations available from the WHO
            documents on the use of NGS for TB
          length: 1h
          other:
            - label: Assessment
              value: "Finished watching the webinar as part of the Mtb NGS training event? Share your thoughts with us [here](https://docs.google.com/document/d/1yCSyBnC1D5-czrW8xUi8sS2ffk_igB7quqhbHr7PE-U/edit#)"
          note: |
            *The completion of this assessment is a requirement for the certificate of attendance.*

      - external:
          title: Q&A session
          description: |
            If you are part of the Mtb NGS training event we would like to hear your opinion on the following questions and promote discussion in this Q&A session. Please let us know your thoughts on one or more of the following questions in the shared notes; 1) How do I choose the right sequencing technology for my samples? 2) What is needed for NGS? 3) Why is NGS better for drug resistance and outbreak analysis? Also take the chance to ask us or write down in the shared notes other questions you might have.

          other:
            - label: Time
              value: "14:00 -16:00 CET"
            - label: Shared notes
              link: https://docs.google.com/document/d/1VtGho4Zz0qFp5tzqD8rl7NU83xtYb4tCkLDitC3DrhQ/edit#
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451
          note: |
            *The completion of this assessment is a requirement for the certificate of attendance.*
  day2:
    title: "Day 2"
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
      resistant patterns, draw phylogenetic relationships or identify clusters of transmission M.
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
          length: 45m
          video: 38GUBKwWXv8
          author: dbrites
          other:
            - label: Assessment
              value: "Finished watching the webinar as part of the Mtb NGS training event? Share your thoughts with us [here](https://docs.google.com/document/d/18y0PScnbA0GuLKjITzIr01wyLVWH6RYPAE5RWkwlfNA/edit#heading=h.bs9dcv9mioqd)"
          note: |
            *The completion of this assessment is a requirement for the certificate of attendance.*

      - external:
          title: Q&A session
          description: Meet the the experts
          author: [dbrites, GaloGS]
          other:
            - label: Time
              value: "11:30-12:30 CET"
            - label: Zoom Link
              link: https://swisstph.zoom.us/j/84656236451
      - self-study: variant-analysis/tb-variant-analysis
        description: Variation in the genome of M. tuberculosis (Mtb) is associated with changes in phenotype, for example drug resistance and virulence. It is also useful for outbreak investigation as the single nucleotide polymorphisms (SNPs) in a sample can be used to build a phylogeny.
        prefix: "Hands-on: "
      - external:
          title: Q&A session
          description: Meet the the experts
          author: [dbrites, GaloGS]
          other:
            - label: Time
              value: "16:30-17:30 CET"
            - label: Zoom Link
              link: https://swisstph.zoom.us/j/84656236451

  day3:
    title: "Day 3"
    description: |
      We are ready to analyse drug resistant patterns, draw phylogenetic relationships or
      identify recent transmission among the isolates we have sampled in our population. Before
      delving into the analysis of the genomes we would like to share with you some notions
      important to the inference of direct transmission and to the interpretation of drug
      resistant patterns.
  day3-1:
    title: "Evolutionary epidemiology: using phylogenetics to understand DR emergence and Mtb transmission"
    trainings:
      - icebreaker:
          - prompt: "What is your favorite dish (food or drink)? Bonus points for recipes!"
            channel: event-mtb-ngs
      - external:
          title: "Webinar: Drug resistance prediction"
          author: GaloGS
          description: Principles of drug resistance detection from genomic data
          length: 20m
          video: Ddwt-_gQR2M
          other:
            - label: Assessment
              value: "Finished watching the webinar as part of the Mtb NGS training event? Share your thoughts with us [here](https://docs.google.com/document/d/1WnvgYtTUOJGxTUEQCL0-HOlHNkqo293LaqaGB9EKojM/edit#heading=h.bs9dcv9mioqd)"
          note: |
            *The completion of this assessment is a requirement for the certificate of attendance.*

      - external:
          title: 'Webinar: "Phylogenetic" mutations'
          author: GaloGS
          description: |
            This video will introduce one special type of mutations to take into account when studying
            drug resistance patterns
          length: 15m
          video: 1ps_o5rpnmw
          other:
            - label: Assessment
              value: "Finished watching as part of the Mtb NGS training event? Share your thoughts with us [here](https://docs.google.com/document/d/1I341zrHJdAn5BEtrtc1KmJZ_x_lez_EWA75iTFBq-R4/edit#)"
          note: |
            *The completion of this assessment is a requirement for the certificate of attendance.*
      - external:
          title: "Webinar: The concept of clustering"
          author: GaloGS
          description: Main aspects of clustering analysis to infer transmission in MTBC
          length: 15m
          video: l4cPUECJ7VU
      - external:
          title: "Webinar: Genetic distance thresholds"
          author: GaloGS
          description: Clustering as an approximation to infer transmission
          length: 15m
          video: kKNgmpy1N94
          other:
            - label: Assessment
              value: "Finished watching as part of the Mtb NGS training event? Share your thoughts with us [here](https://docs.google.com/document/d/1Q4mw-y3FZrGvmz3VNQrLkLslsi5QoTgDxwhAYYYdvjI/edit#)"
          note: |
            *The completion of this assessment is a requirement for the certificate of attendance.*

      - self-study: evolution/mtb_transmission
        description: Learning how to do clustering analysis and interpret drug resistance patterns
        prefix: "Hands-on: "

      - external:
          title: Q&A
          description: Discussion with the experts
          author: [GaloGS,cstritt]
          other:
            - label: Time
              value: "11:30-12:30 CET"
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451

      - external:
          title: "Introduction to phylogenetics"
          author: embl-ebi
          description: "Recommended to those wanting to learn more about phylogenetics"
          length: 1h
          tutorial: "https://www.ebi.ac.uk/training/online/courses/introduction-to-phylogenetics/"

      - self-study: evolution/mtb_phylogeny
        description: Main principles of phylogenetic inference, tree interpretation
        prefix: "Hands-on: "

      - external:
          title: "Check what you have learnt!"
          description: "We hope that you are enjoying the training, and that many things that you are learning will be useful for your research! We would like you to answer some questions, so both you and us, can assess whether the main concepts covered in the hands-on tutorials on Mtb NGS data analysis were understood. For that please follow the link bellow. If you are interested in knowing what we think about these questions join us on Day 5"
          other:
            - label: Assessment
              link: https://docs.google.com/document/d/1mT6z84iA2-E2D834lH1B6fJrWwfXYBKDkPrKCFAdwqk/edit#
          note: |
            *The completion of this assessment is a requirement for the certificate of attendance.*


      - external:
          title: Q&A
          author: [GaloGS,cstritt]
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
          author: arashghodousi
          description: Introduction to most common web tools for fast identification of bacterial species from raw sequencing reads
          length: 50m
          video: HVQaq2GXCAc
          other:
            - label: Assessment
              value: "Finished watching as part of the Mtb NGS training event? Share your thoughts with us [here](https://docs.google.com/document/d/1jdp61AFeyd_fK8XWZ348k7aok779feiCQ3q2uz1RPF0/edit#)#"
          note: |
            *The completion of this assessment is a requirement for the certificate of attendance.*
      - external:
          title: "Webinar: Introduction to the MTBseq pipeline"
          author: arashghodousi
          description: Introduction to MTBseq pipeline, an automated pipeline for mapping, variant calling and detection of resistance mediating and phylogenetic variants from whole genome sequence data of MTBC
          length: 30m
          video: ob29WYXwLxo

      - external:
          title: Q&A
          description: Meet the the experts
          author: andreaspitaleri
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
          author: andreaspitaleri
          description: "Introduction to Linux OS: installation and usage"
          length: 35m
          video: N8rW07ByQOE
      - external:
          title: "Webinar: How to run programs (Python, Docker, Nextflow)"
          author: andreaspitaleri
          description: Learning how to install and use programs to analyze data
          length: 35m
          video: feYweAQNGS8
      - external:
          title: "Webinar: Demo on how to run the Linux command line"
          author: andreaspitaleri
          description:   Demo video on how to use the shell commands
          length: 20m
          video: 7V7LCjUEg1c
      - external:
          title: "Hands-on: The Unix Shell"
          author: thecarpentries
          description: Recommended tutorial from software carpentries to those wanting to learn Linux.
          length: 4h
          tutorial: "https://swcarpentry.github.io/shell-novice/"
      - external:
          title: Q&A
          description: Discussion with the experts
          author: [arashghodousi,andreaspitaleri]
          other:
            - label: Time
              value: "16:30-17:30 CET"
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451

  day5:
    title: Day 5
    description: |
      Today all experts will  be available to answer your questions and discuss any
      of the tutorials, webinars, or questions related to your own data. Meet with us at the
      zoom link!
    trainings:
      - external:
          title: Q&A
          description: Discussion with the experts
          author: [dbrites,cstritt,andreacabibbe,annalenaguske, andreaspitaleri,GaloGS,arashghodousi,liliana-rutaihwa]
          other:
            - label: Time
              value: "10:00-12:30 CET"
            - label: Zoom
              link: https://swisstph.zoom.us/j/84656236451

  wrapup:
    title: Wrap-up
    trainings:
      - feedback
      - certificates

---
