# Project 8 – Variant Calling and Functional Annotation Using Galaxy

## Overview

This project implements an end-to-end next-generation sequencing (NGS) variant-analysis workflow using **Galaxy**. Raw paired-end Illumina sequencing reads were processed through quality control, trimming, alignment to the human reference genome, variant calling, read-level visualization, and functional annotation.

The workflow identified **37 PASS variants** across chromosomes 1, 17, and the mitochondrial genome and used SnpEff to predict their potential molecular consequences.

---

## Workflow

**Paired-end FASTQ reads → FastQC → Trimmomatic → BWA-MEM → LoFreq → IGV → SnpEff**

- **FastQC** – assessed the quality of the raw sequencing reads
- **Trimmomatic** – removed low-quality sequence regions
- **BWA-MEM** – aligned paired reads to the hg38 human reference genome
- **LoFreq** – detected sequence variants and generated a VCF file
- **IGV** – provided read-level visualization of selected variants
- **SnpEff** – annotated predicted functional consequences using GRCh38.115

---

## Key Results

- Identified **37 PASS variants**: 2 on chromosome 1, 6 on chromosome 17, and 29 in the mitochondrial genome.
- Examined read-level support for a high-confidence **chr17 G→A** variant using IGV.
- Functionally annotated detected variants with **SnpEff 5.4c**.
- Identified predicted missense, synonymous, intronic, intergenic, and non-coding transcript effects.
- Resolved a mitochondrial chromosome-naming incompatibility (`chrM` → `MT`) between the variant file and SnpEff database.

---

## Tools & Technologies

**Galaxy · FastQC · Trimmomatic · BWA-MEM · LoFreq · IGV · SnpEff · VCF · BAM · hg38/GRCh38**

---

## Dataset

**Training material for Calling Variants in Non-diploid Systems**

https://zenodo.org/record/1251112

---

## Skills Demonstrated

- NGS data processing
- Paired-end Illumina sequencing analysis
- Sequencing quality control
- Read trimming and preprocessing
- Reference genome alignment
- Variant calling and VCF interpretation
- Read-level variant visualization
- Functional variant annotation
- Bioinformatics troubleshooting
- Reference and chromosome nomenclature harmonization

---

## Project Details

Detailed methodology, results, figures, variant interpretation, and SnpEff annotation results are available in **`results.md`**.
