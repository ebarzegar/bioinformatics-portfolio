# Variant Calling Workflow Using Galaxy

## Introduction

In this project, a complete next-generation sequencing (NGS) variant-calling workflow was performed using the Galaxy platform. Raw paired-end Illumina sequencing reads obtained from the Zenodo training dataset were processed through several analysis steps, including quality assessment, read trimming, sequence alignment, variant detection, visualization, and functional annotation.

### Data Acquisition

Raw Illumina paired-end sequencing reads were obtained from the Zenodo "Training material for Calling variants in non-diploid systems" repository. For this project, the paired-end child dataset (raw_child-ds-1.fq and raw_child-ds-2.fq) was selected as the input data for the variant-calling workflow. These FASTQ files contain forward (Read 1) and reverse (Read 2) sequencing reads that are analyzed together throughout the pipeline.

Dataset:
https://zenodo.org/record/1251112
## Step 2 – Quality Assessment

Before sequence alignment, the quality of the raw sequencing reads was evaluated using FastQC. This quality-control step identifies potential sequencing issues such as low-quality bases, GC content bias, duplicated reads, adapter contamination, and sequence length distribution. Detecting these problems before downstream analysis helps ensure that only high-quality sequencing data are used for variant calling.
The quality of the raw paired-end Illumina sequencing reads was evaluated using the FastQC tool available in the Galaxy platform. FastQC generates several quality-control metrics, including per-base sequence quality, GC content, sequence length distribution, duplicated sequences, and adapter contamination. These quality reports help identify potential sequencing problems before downstream analysis.

Both paired-end FASTQ files were analyzed independently to evaluate their sequencing quality.
## Step 2 – Quality Assessment with FastQC

The quality of the raw paired-end sequencing reads was evaluated using FastQC within the Galaxy platform. The FastQC report provides several quality-control metrics, including per-base sequence quality, sequence composition, GC content, sequence duplication, and sequence length distribution.

The per-base quality plot showed that most bases had Phred quality scores above 30 throughout the majority of each read, indicating high-confidence sequencing data. As expected for Illumina sequencing, the quality gradually decreased toward the 3′ end of the reads. This reduction in quality supports the need for a trimming step before sequence alignment.

Some FastQC modules generated warnings or failures (e.g., sequence duplication and per-base sequence content), which are common characteristics of high-throughput sequencing datasets and were addressed during the preprocessing stage.
<img width="1530" height="602" alt="image" src="https://github.com/user-attachments/assets/04ffd03e-d56e-435c-a563-ce5604ad3698" />

FastQC quality assessment of the raw Illumina sequencing reads showing high base quality across most of the read length with a gradual decrease toward the 3′ end.
