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
    title: "Building a pathogen surveillance system"
    #description: TODO description
    trainings:
      - video: sars-cov2/using-galaxy
      - video: variant-analysis/sars-cov-2-variant-discovery/tutorial
      - video: galaxy-interface/workflow-automation
      - video: sars-cov2/usegalaxy-star-bot

  archiving:
    title: Pathogen data sharing and archiving
    #description: TODO description
    trainings:
      - video: assembly/assembly-with-preprocessing
      - video: sars-cov2/upload-ena
      - video: galaxy-interface/upload-to-ena
---

'One Health' is an integrated, unifying approach to balance and optimize the health of people, animals and the environment. It is particularly important to prevent, predict, detect, and respond to global health threats such as the COVID-19 pandemic.

The approach mobilizes multiple sectors, disciplines and communities at varying levels of society to work together. This way, new and better ideas are developed that address root causes and create long-term, sustainable solutions.

One Health involves the public health, veterinary and environmental sectors. The One Health approach is particularly relevant for food and water safety, nutrition, the control of zoonoses (diseases that can spread between animals and humans, such as flu, rabies and Rift Valley fever), pollution management, and combatting antimicrobial resistance (the emergence of microbes that are resistant to antibiotic therapy).
