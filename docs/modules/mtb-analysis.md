---
layout: module
title: "Mycobacterium tuberculosis NGS made easy: data analysis step-by-step"
description: "Webinars and hands-on tutorials on several aspects related to NGS in Tuberculosis"


program:
  intro:
    title: Introduction
    description: |
      There were unusually high rates of TB cases in your country this year. To characterize the underlying
      bacterial factors driving the epidemic, isolates have been sent for whole-genome sequencing.  Doctors and public
      health authorities request information in order to take decisions. In this course it will be demonstrated how
      you would make use of NGS to answer several questions relevant for patient and public health system management
      such as:
        - Are there cases of drug resistant bacteria?
        - Is there transmission of drug resistance?
        - Is there evidence of de novo emergence of resistance?
        - Are there multiple infections per patient?
        - Do we have on-going transmission?

      We hope that at the end of the different training sessions you can answer this question on your own!

  day1:
    title: "Part 1 - Overview of NGS technologies & TB specific NGS solutions"

  day1-1:
    title:
    subday: true

    trainings:
      - external:
          title: "Webinar: Overview of NGS technologies & TB specific NGS solutions"
          description: |
            This webinar will introduce different sequencing technologies and what applies best to what
            kind of problem.
          video: BcfBjCJRmUs
          length: 1h10m
          author: andreacabibbe
          feedback: https://docs.google.com/document/d/1Jl9mm5u91_ayub7RPnE4pL2vobgaMDDa3UaD4nFH-aQ/edit#
          other:
            - label: Feedback
              link: "https://docs.google.com/document/d/1Jl9mm5u91_ayub7RPnE4pL2vobgaMDDa3UaD4nFH-aQ/edit#"
      - external:
          title: "Webinar: Implementation of NGS for TB- WHO documents and other considerations"
          author: andreacabibbe
          video: eSWnPange8w
          description: |
            This webinar will summarize the recommendations and considerations available from the WHO
            documents on the use of NGS for TB
          length: 1h
          other:
           - label: Feedback
             link: https://docs.google.com/document/d/10z_XWJ8Q4j8PHZe2KHmRnfLrjjAC07aRDy-aD5SOIAE/edit#heading=h.bs9dcv9mioqd
      - external:
           title: "FAQs"
           table: "no"
           description: |
             For a list of frequently asked questions, please refer to [this document](https://docs.google.com/document/d/1PyFY80m05tiqBbEhW6H-VRZdXPjkA2rFfsPey5ujzy4/edit?usp=sharing)


  day2:
    title: "Part 2 - Mapping and Variant calling of short MTBC reads "
    description: |
      The 20 strains isolated in your country have been sequenced with Illumina technology
      to obtain whole-genome sequences. In this part of the workshop you will learn how to
      analyse those sequences.

      In a typical bioinformatic pipeline you would store your sequences in a computer server
      where all necessary software would be installed. This would be a server running the
      operating system LINUX, which is the most efficient way to run bioinformatics pipelines
      (more on this on Part 5). You will be running your analysis in a LINUX server from Galaxy,
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

  day2-1:
    title: "Session 1: Learning Galaxy"
    subday: true
    trainings:
      - video: galaxy/intro
      - video: introduction/galaxy-intro-101/tutorial

  day2-2:
    title: "Session 2: Mapping and Variant calling of short MTBC reads -hands-on"
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
            - label: Feedback
              link: https://docs.google.com/document/d/1ofjUVvfA1j1sCbIQKyiZAfYvB8JDo16MAgQ7xLV_eD0/edit#
      - external:
           title: "FAQs"
           table: "no"
           description: |
             For a list of frequently asked questions, please refer to [this document](https://docs.google.com/document/d/1bfzkxrgDUu-knISuyklwqqAo7B2uPTpWCfAN7AbawhE/edit?usp=sharing)

      - self-study: variant-analysis/tb-variant-analysis
        description: |
          Variation in the genome of M. tuberculosis (Mtb) is associated with changes in phenotype, for example drug resistance and virulence.
          It is also useful for outbreak investigation as the single nucleotide polymorphisms (SNPs) in a sample can be used to build a phylogeny.
        prefix: "Hands-on: "

  day3:
    title: "Part 3 - Evolutionary epidemiology: using phylogenetics to understand DR emergence and Mtb transmission"
    description: |
      We are ready to analyse drug resistant patterns, draw phylogenetic relationships or
      identify recent transmission among the isolates we have sampled in our population. Before
      delving into the analysis of the genomes we would like to share with you some notions
      important to the inference of direct transmission and to the interpretation of drug
      resistant patterns.
  day3-1:
    title:
    trainings:
      - external:
          title: "Webinar: Drug resistance prediction"
          author: GaloGS
          description: Principles of drug resistance detection from genomic data
          length: 20m
          video: Ddwt-_gQR2M
          other:
            - label: Feedback
              link: https://docs.google.com/document/d/1FM1CBF1wEMyTU9KHSG_3wSEM5zCY3R_GqPRCmtvW18g/edit?usp=sharing

      - external:
          title: 'Webinar: "Phylogenetic" mutations'
          author: GaloGS
          description: |
           This video will introduce one special type of mutations to take into account when studying
           drug resistance patterns
          length: 15m
          video: 1ps_o5rpnmw
          other:
            - label: Feedback
              link: https://docs.google.com/document/d/1_g-S-Qb19_DUAIfBETJ8V6Yt43-h3dpIq7Crr7upxZY/edit?usp=sharing
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
            - label: Feedback
              link: https://docs.google.com/document/d/1XZdRSHvLdxX-KKirgVhNoAV8cD416s18FTEh-Nz5JIQ/edit?usp=sharing

      - self-study: evolution/mtb_transmission
        description: Learning how to do clustering analysis and interpret drug resistance patterns
        prefix: "Hands-on: "

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
          title: "FAQs"
          table: "no"
          description: |
            For a list of Frequently Asked Quetions, please refer to [this document](https://docs.google.com/document/d/1QRdTSVdXQm8Fafnl3fqf2ZKJxJZiAdeZOUCT0dTRmx4/edit?usp=sharing)


  day4:
    title: Part 4 - Webtools dedicated to MTBC bioinformatics

  day4-1:
    title:
    subday: true
    description: |
      The use of whole-genome sequencing (WGS) for antibiotic resistance prediction and routine
      typing of bacterial isolates has increased substantially in recent years. To date a
      multitude of solutions for analyzing WGS data of the Mycobacterium tuberculosis complex
      (MTBC) data have been developed. In the first 4th part, we
      introduce some freely available webtools and open source pipelines designed to analyze
      MTBC sequence data and we’ll provide some examples of how these tools work and how to
      interpret the results.
    trainings:
      - external:
          title: "Webinar: Web tools for analysis of MTBC sequenced data"
          author: arashghodousi
          description: Introduction to most common web tools for fast identification of bacterial species from raw sequencing reads
          length: 50m
          video: HVQaq2GXCAc
          other:
            - label: Feedback
              link: https://docs.google.com/document/d/1SxLlaN5Bg6PhV2cz6VLr1ptEP5kjNK1stjIVVCrSqSw/edit?usp=sharing
      - external:
          title: "Webinar: Introduction to the MTBseq pipeline"
          author: arashghodousi
          description: Introduction to MTBseq pipeline, an automated pipeline for mapping, variant calling and detection of resistance mediating and phylogenetic variants from whole genome sequence data of MTBC
          length: 30m
          video: ob29WYXwLxo
      - external:
          title: "FAQs"
          table: "no"
          description: |
            For frequently asked questions, please see [this document](https://docs.google.com/document/d/1rl4ZAmTXiEVNIKIwomAAoi-EMcRmulat_S0KPrlI3aw/edit?usp=sharing)

  day5:
    title: Part 5 - Be a bioinformatician in the jungle
    description: |
      On parts 2 and 3 of this training you have learned how you could use galaxy for analysing your own data.
      Establishing your own workflows in galaxy would allow you combining different tools and
      build your own pipeline without having to know how to program. If you are not so
      interested in having your own pipeline, webtools for WGS analysis can be very useful, as
      we have shown in part 4.

      However, in this last part of the training we would like to convey to you what it would
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


---

