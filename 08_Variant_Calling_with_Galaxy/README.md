# Project 8 – Variant Calling Workflow Using Galaxy

## Overview

This project demonstrates a complete next-generation sequencing (NGS) variant-calling workflow using the Galaxy platform. Starting from raw Illumina paired-end sequencing reads, the workflow performs quality control, read trimming, sequence alignment, variant detection, visualization, and functional annotation to identify genomic variants.

The project illustrates how multiple bioinformatics tools can be integrated into a reproducible workflow for analyzing high-throughput sequencing data.

---

## Learning Objectives

- Understand Illumina paired-end sequencing data
- Perform quality assessment using FastQC
- Trim low-quality sequencing reads with Trimmomatic
- Align sequencing reads to a reference genome using BWA-MEM
- Detect genomic variants using LoFreq
- Visualize alignments and variants using IGV
- Annotate variants using SnpEff
- Understand the complete workflow used in modern NGS variant analysis

---

## Workflow

1. Download paired-end sequencing reads from Zenodo.
2. Import sequencing data into Galaxy.
3. Evaluate read quality using FastQC.
4. Trim low-quality bases using Trimmomatic.
5. Align reads to the reference genome using BWA-MEM.
6. Detect sequence variants using LoFreq.
7. Visualize alignments and variants in IGV.
8. Annotate variants using SnpEff.

---

## Tools Used

- Galaxy
- FastQC
- Trimmomatic
- BWA-MEM
- LoFreq
- IGV
- SnpEff

---

## Dataset

Training material for Calling Variants in Non-diploid Systems

https://zenodo.org/record/1251112

---

## Skills Demonstrated

- Next-generation sequencing (NGS)
- Illumina paired-end sequencing
- FASTQ file processing
- Sequencing quality control
- Read trimming
- Sequence alignment
- Variant calling
- Variant visualization
- Variant annotation
- Reproducible bioinformatics workflows

---

## Summary

This project demonstrates how raw sequencing reads are transformed into biologically meaningful variant information through a standard NGS analysis pipeline. Each tool contributes a specific stage of the workflow, beginning with sequencing quality assessment and ending with functional annotation of detected variants. Together, these steps represent a typical variant-calling pipeline widely used in bioinformatics and genomics research.
