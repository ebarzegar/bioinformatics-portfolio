This project demonstrates a complete variant-calling workflow using the Galaxy platform. Starting from raw Illumina sequencing reads, quality control, read trimming, sequence alignment, variant detection, and functional annotation were performed to identify genomic variants. The workflow introduces the fundamental steps commonly used in next-generation sequencing (NGS) analysis and illustrates how web-based bioinformatics tools can be combined into a reproducible analysis pipeline.

explaining Illumina/NGS reads and paired-end sequencing,
importing sequencing files and a reference genome into Galaxy,
mapping reads to the reference with BWA-MEM,
checking read quality with FastQC,
trimming low-quality bases with Trimmomatic,
calling variants with LoFreq,
viewing alignments and variants in IGV,
and annotating variants using SnpEff.


Dataset (Zenodo + Galaxy upload)
FastQC
Trimmomatic
BWA-MEM
LoFreq
IGV
SnpEff

The workflow demonstrates how raw sequencing reads are progressively transformed into biologically meaningful variant information. Each tool performs a specific role within the pipeline, from assessing sequencing quality to annotating the potential biological effects of detected variants
