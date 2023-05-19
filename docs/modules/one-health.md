---
layout: module
title: One Health

program:
  viral:
    title: "Viral Pathogen Analysis"
    #description: TODO description (if useful)
    trainings:
      - video: virology/sequencing-spectrum-viral-genomes
      - video: variant-analysis/sars-cov-2
      - self-study: variant-analysis/aiv-analysis
      - self-study: variant-analysis/pox-tiled-amplicon # title will appear once tutorial is merged into GTN

  tb:
    title: Tuberculosis Sequence Analysis
    #description: TODO description
    trainings:
      - external:
          title: "Webinar: Implementation of NGS for TB- WHO documents and other considerations"
          author: andreacabibbe
          video: eSWnPange8w
          description: |
            This webinar will summarize the recommendations and considerations available from the WHO
            documents on the use of NGS for TB
          length: 1h
      - session: variant-analysis/tb-variant-analysis
      - external:
          title: "Webinar: Drug resistance prediction"
          author: GaloGS
          description: Principles of drug resistance detection from genomic data
          length: 20m
          video: Ddwt-_gQR2M
      - external:
          title: 'Webinar: "Phylogenetic" mutations'
          author: GaloGS
          description: |
           This video will introduce one special type of mutations to take into account when studying
           drug resistance patterns
          length: 15m
          video: 1ps_o5rpnmw
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

  surveillance:
    title: "Building a pathogen surveillance system with Galaxy"
    description: |
      Learn how to integrate Galaxy-based pathogen sequence data analysis into
      molecular surveillance programs
    trainings:
      - video: one-health/galaxy-pathogen-surveillance
      - video: variant-analysis/sars-cov-2-variant-discovery/tutorial
      - video: galaxy-interface/workflow-automation
      - video: sars-cov2/usegalaxy-star-bot
      - self-study: sequence-analysis/tutorials/human-reads-removal
      - video: sars-cov2/upload-ena
---

"One Health" is an integrated, unifying approach to balance and optimize the health of people, animals and the environment. It is particularly important to prevent, predict, detect, and respond to global health threats such as the COVID-19 pandemic.

The approach mobilizes multiple sectors, disciplines and communities at varying levels of society to work together. This way, new and better ideas are developed that address root causes and create long-term, sustainable solutions.

One Health involves the public health, veterinary and environmental sectors. One focus area of the One Health approach is the control of zoonoses (diseases that can spread between animals and humans), such as those caused by coronaviruses, influenza, pox viruses, or bacteria of the Mycobacterium tuberculosis complex.
