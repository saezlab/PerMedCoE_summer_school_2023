# From transcriptomics to mechanistic models of signalling
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saezlab/PerMedCoE_tools_virtual_course_2023/blob/main/PerMedCoE_transcriptomics_mechanistic_signaling.ipynb)

This repository contains the material for the [PerMedCoE virtual course: transcriptomics to mechanistic models of signalling](https://permedcoe.eu/training/virtual-course-from-transcriptomics-to-mechanistic-models-of-signalling/). The `PerMedCoE_transcriptomics_mechanistic_signaling.ipynb` notebook included in the repository is self-contained document with explanations and code to run on your own or using Google Colab. The course has an estimated duration of ~3h.

## Overview

Cellular signalling networks are the communication pathways that govern the behaviour of cells. They allow cells to receive and process external signals, such as growth factors and hormones, and respond appropriately by activating specific gene expression programs or inducing cellular behaviours like proliferation, migration, and differentiation. Disruptions in these signalling networks can lead to various diseases, including cancer, metabolic disorders, and immune disorders. Understanding the regulatory mechanisms of signalling networks is critical to developing effective therapies for these diseases.

One approach to discover signalling network alterations from omics data is through the use of upstream regulatory pathway analysis, which aims to identify the transcription factors and upstream signalling regulators that control the expression of downstream genes. This can be achieved through the joint analysis of omics data and the signalling network structure using methods such as CARNIVAL. By using powerful algorithms and general purpose integer optimization solvers, CARNIVAL explores the vast space of potential signalling alterations to identify a parsimonious signalling network that explains the measurements.

In this course, participants will learn how to process differential gene expression data to estimate transcription factor activities with DecoupleR, obtain and process prior knowledge networks with OmniPath and pypath, and use CARNIVAL to infer signalling networks.

## Learning outcomes
At the end of these sessions, the participants will be able to:

- Obtain custom networks of causal interactions from public databases
- Combine these networks with molecular biological activities from experimental data
- Apply causal reasoning to find the most plausible causal mechanisms that explain the observed activity patterns
- Use CARNIVAL to customise the contextualisation of signalling networks

## Audience
Number of participants: 25.

This course is aimed at researchers who work in systems level molecular biology or biomedicine, and are interested in extracting mechanistic insights from transcriptomics data. Pre-requisites:

We expect the participants to have a basic understanding of the following topics: scripting in Python and R, transcriptomics data analysis, molecular networks, constraint-based optimisation.
The course will be delivered in a Google Colaboratory notebook with the necessary tools pre-installed.

## Registration
You can apply to the course [here](https://www.eventsforce.net/embl/frontend/reg/thome.csp?pageID=57622&eventID=94&traceRedir=2). Registration is free. Applications are first-come first-served based and we will review applications on a rolling basis to select suitable candidates until the 25 places available are filled. A waiting list will be established if needed.

## How the course will run
The course will take place virtually in Zoom on Tuesday 18 April 2023, 13 - 16 h CEST, including breaks. The training will combine lectures and hands-on exercises, and participants are expected to attend the whole course.

## Trainers
- Pablo Rodriguez Mier*
- Denes Turei*

>*Saez-Rodriguez Group, Institute for Computational Biomedicine, Heidelberg University


If you have any questions or comments, you can contact Daniel Thomas López (dthlopez@ebi.ac.uk).
Visit PerMedCoE website to read about our activities, including training events, materials, and webinars.

<img src="https://raw.githubusercontent.com/saezlab/.github/main/profile/logos/saezlab.png" alt="Saez lab logo" height="64px" style="height:64px; width:auto"> <img src="https://lcsb-biocore.github.io/COBREXA.jl/stable/assets/permedcoe.svg" alt="PerMedCoE logo" height="64px" style="height:64px; width:auto"> <img src="https://www.klinikum.uni-heidelberg.de/typo3conf/ext/site_ukhd/Resources/Public/Images/Logo_ukhd_de.svg" alt="UKHD logo" height="64px" style="height:64px; width:auto">  
