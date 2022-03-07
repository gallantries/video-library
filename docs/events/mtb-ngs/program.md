---
layout: program
module: false
title: "Mycobacterium tuberculosis NGS made easy: data analysis step-by-step"
certbot: false
instructors: [danielabrites]
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
      - setup
      - code-of-conduct

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
         - prompt: "Introduce yourself and tell us your favorite science fun fact!"
           channel: "event-mtb-ngs"
      - external:
          title: "Webinar: Overview of NGS technologies & TB specific NGS solutions"
          description: |
            This webinar will introduce different sequencing technologies and what applies best to what
            kind of problem.
          video: todo
          length: 1h15m
          author: Andrea Cabibbe

      - external:
          title: "Webinar: Implementation of NGS for TB- WHO documents and other considerations"
          author: Andrea Cabibbe
          video: todo
          description: |
            This webinar will summarize the recommendations and considerations available from the WHO
            documents on the use of NGS for TB
          time: 1h
      - external:
          title: Q&A session
          description: Discussion. Q&A join the experts
          other:
            - label: Zoom (TODO)
              link: TODO


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
        - prompt: TODO
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
          time: 45m
          slides: "https://docs.google.com/presentation/d/1Q3es-gIoMJ_otl_Wbd-JKZThhnZxZdL3gcYmRFJiAeU/edit?usp=sharing"
          author: Daniela Brites
      - external:
          title: Q&A session
          description: Discussion with the experts
          author: Daniela Brites & Galo A. Goig
          other:
            - label: Time
              value: "11:30-12:30 CET"
            - label: Zoom Link (TODO)
              link: TODO
      - session: variant-analysis/tb-variant-analysis
      - external:
          title: Q&A session
          description: Discussion with the experts
          author: Daniela Brites & Galo A. Goig
          other:
            - label: Time
              value: "16:30-17:30 CET"
            - label: Zoom Link (TODO)
              link: TODO

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
        - prompt: TODO
          channel: event-mtb-ngs
      - external:
          title: "Webinar: Drug resistance prediction"
          author: Galo A. Goig
          description: Principles of drug resistance detection from genomic data
          length: 20m
          video: todo
      - external:
          title: "Webinar: Phylogenetic and compensatory mutations"
          author: Galo A. Goig
          description: |
            This video will introduce two types of mutations to take into account when studying
            drug resistance patterns
          length: 15m
          video: todo
      - external:
          title: "Webinar: The concept of clustering"
          author: Galo A. Goig
          description: Main aspects of clustering analysis to infer transmission in MTBC
          length: 15m
          video: todo
      - external:
          title: "Webinar: Genetic distance thresholds"
          author: Galo A. Goig
          description: Clustering as an approximation to infer transmission
          length: 15m
          video: todo
      - external:
          title: "Hands-on: Performing clustering analysis & drug resistance prediction"
          author: Galo A. Goig
          description: Learning how to do clustering analysis and interpret drug resistance patterns
          length: 2h
          video: todo
      - external:
          title: Q&A
          description: Discussion with the experts
          author: Galo A. Goig & Christoph Stritt
          other:
            - label: Time
              value: "11:30-12:30 CET"
            - label: Zoom (TODO)
              link: TODO

      - external:
          title: "Hands-on: Inference of phylogenetic trees"
          description: Main principles of phylogenetic inference, tree interpretation
          author: Christoph Stritt
          length: 1h
          video: todo
      - external:
          title: Q&A
          author: Galo A. Goig & Christoph Stritt
          description: Discussion with the experts
          other:
            - label: Time
              value: "16:30-17:30 CET"
            - label: Zoom (TODO)
              link: TODO

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
        - prompt: TODO
          channel: event-mtb-ngs
      - external:
          title: "Webinar: Fast identification of bacterial strains from raw sequencing reads"
          author: Arash Ghodousi
          description: Introduction to most common web tools for fast identification of bacterial species from raw sequencing reads
          length: 30m
          video: todo
      - external:
          title: "Webinar: Web tools for analysis of MTBC sequenced data"
          author: Arash Ghodousi
          description: This video will introduce web tools designed for analysis of MTBC sequenced data
          length: 45m
          video: todo
      - external:
          title: "Webinar: Introduction to the MTBseq pipeline"
          author: Arash Ghodousi
          description: Introduction to MTBseq pipeline, an automated pipeline for mapping, variant calling and detection of resistance mediating and phylogenetic variants from whole genome sequence data of MTBC
          length: 30m
          video: todo
      - external:
          title: "Webinar: Demonstration of data analysis using webtools"
          author: Arash Ghodousi
          description: Demonstration of how to use most common web tools for analysis of MTBC sequenced data
          length: 45m
          video: todo
      - external:
          title: Q&A
          description: Discussion with the experts
          author: Arash Ghodousi & Andrea Spitaleri
          other:
            - label: Time
              value: "11:30-12:30 CET"
            - label: Zoom (TODO)
              link: TODO

  day4-2:
    title: "Session 2: Be a bioinformatician in the jungle"
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
          length: 30m
          video: todo
      - external:
          title: "Webinar: How to run programs (Python, Docker, Singularity)"
          author: Andrea Spitaleri
          description: Learning how to install and use programs to analyze data
          length: 30m
          video: missing
      - external:
          title: "Webinar: Demo on how to run the Linux command line"
          author: Andrea Spitaleri
          description:   Demo video on how to use the shell commands
          length: 30m
          video: todo
      - external:
          title: "[Optional] Hands-on: The Unix Shell"
          author: Andrea Spitaleri
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
            - label: Zoom (TODO)
              link: TODO

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
            - label: Zoom (TODO)
              link: TODO

---
