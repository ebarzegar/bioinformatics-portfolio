# Multiple Sequence Alignment of Lactobacillus 16S rRNA Sequences

## Project Overview

This project compares the **16S ribosomal RNA (16S rRNA)** sequences of five *Lactobacillus* species using multiple sequence alignment (MSA).

The objective was to identify conserved and variable nucleotide positions and visualize sequence conservation using a sequence logo (WebLogo).

This project was originally completed as part of my undergraduate Bioinformatics coursework and has been reconstructed as a professional portfolio project.

---

## Biological Background

The **16S rRNA** gene is one of the most widely used molecular markers for bacterial identification and phylogenetic analysis because it contains both highly conserved and variable regions. Conserved regions allow comparison across species, while variable regions help distinguish closely related organisms.

---

## Species Included

| Species | RefSeq Accession |
|----------|------------------|
| *Lactobacillus helsingborgensis* | NR_126253.1 |
| *Lactobacillus melliventris* | NR_126252.1 |
| *Lactobacillus kullabergensis* | NR_126251.1 |
| *Lactobacillus kimbladii* | NR_126250.1 |
| *Lactobacillus ultunensis* | NR_042802.1 |

---

## Workflow

1. Retrieved 16S rRNA reference sequences from **NCBI Nucleotide**.
2. Performed multiple sequence alignment using **Clustal Omega**.
3. Visualized the alignment to examine conserved and variable nucleotide positions.
4. Selected a semi-conserved 50-nucleotide region.
5. Generated a sequence logo using **WebLogo**.

---

## Bioinformatics Tools

- NCBI Nucleotide
- Clustal Omega
- WebLogo
- UGENE (alignment visualization)

---

## Results Summary

The multiple sequence alignment demonstrated that the five *Lactobacillus* species share highly conserved regions within the 16S rRNA gene while also containing several variable nucleotide positions.

A semi-conserved 50-nucleotide region was extracted from the alignment and used to generate a WebLogo, illustrating nucleotide conservation across all five species.

Representative screenshots of the beginning and end of the alignment, together with the WebLogo, are included in the **images** folder.

---

## Skills Demonstrated

- Biological sequence retrieval
- Multiple sequence alignment (MSA)
- Comparative genomics
- Sequence conservation analysis
- Sequence logo generation
- Interpretation of conserved and variable nucleotide positions
