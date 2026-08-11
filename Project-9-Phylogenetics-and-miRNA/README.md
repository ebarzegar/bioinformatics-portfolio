# Project 9 – TPI Phylogenetics and Ovarian-Cancer miRNA Analysis

## Overview

This project combines two bioinformatics analyses: **protein phylogenetics** and **miRNA differential-expression analysis**.

Triosephosphate isomerase (TPI) protein sequences from eight organisms were compared using two phylogenetic approaches, UPGMA and Maximum Parsimony, to investigate evolutionary relationships across mammals, plants, fungi, and bacteria.

The second part analyzes the **GSE43867 ovarian-cancer miRNA expression dataset** to investigate miRNAs associated with chemotherapy response. Differentially expressed miRNAs were identified, compared with findings from the original publication, and evaluated through downstream target-prediction analysis.

---

## Analysis Workflow

### Part 1 – TPI Phylogenetic Analysis

TPI protein sequences from eight organisms were collected and compared:

- *Homo sapiens*
- *Oryctolagus cuniculus*
- *Mus musculus*
- *Arabidopsis thaliana*
- *Brettanomyces bruxellensis*
- *Dickeya/Musicola paradisiaca* Ech703
- *Salmonella enterica*
- *Staphylococcus aureus*

Protein sequences were aligned and evolutionary relationships were reconstructed using:

- **UPGMA**
- **Maximum Parsimony**

The resulting trees were compared to evaluate relationships among TPI proteins across the selected species.

### Part 2 – miRNA Differential-Expression Analysis

The **GSE43867** dataset was analyzed using normalized miRNA expression data from:

- **48 chemotherapy responders**
- **38 non-responders**

Differential expression was evaluated using the historical selection criteria:

- `P < 0.05`
- `|logFC| > 1`

Benjamini-Hochberg adjusted P-values were also evaluated to account for multiple testing.

---

## Key Results

### Phylogenetic Analysis

- Human TPI clustered most closely with rabbit and mouse TPI.
- *Dickeya/Musicola paradisiaca* Ech703 clustered with *Salmonella enterica*.
- The two phylogenetic approaches provided complementary representations of evolutionary relationships among the eight TPI proteins.

### miRNA Analysis

Three miRNAs met the nominal differential-expression criteria:

| miRNA | logFC | P-value |
|---|---:|---:|
| hsa-miR-592 | 1.390 | 0.0022 |
| hsa-miR-642 | -1.020 | 0.0090 |
| hsa-miR-483-5p | -1.355 | 0.0160 |

**hsa-miR-592** showed higher expression in chemotherapy responders, whereas **hsa-miR-642** and **hsa-miR-483-5p** showed lower expression in responders.

None of the three candidates remained significant after Benjamini-Hochberg multiple-testing correction; therefore, these findings are treated as **exploratory rather than definitive biomarkers**.

The results were compared with the original publication and previous TargetScan-based target predictions to examine differences between the reproduced analysis and the published findings.

---

## Data Sources

### Protein Sequences

TPI protein sequences were retrieved from **UniProtKB** and **NCBI Protein**. Reviewed records were preferred when available.

For *Arabidopsis thaliana*, the **cytosolic TPI protein (P48491)** was selected rather than the chloroplast isoform to maintain a comparable cellular context across the analyzed proteins.

### miRNA Expression Data

Normalized expression data were obtained from **NCBI GEO accession GSE43867**. Complete and partial chemotherapy responses were classified as responders, while stable disease and no response were classified as non-responders.

---

## Tools & Methods

- Python
- Protein sequence alignment
- UPGMA phylogenetic reconstruction
- Maximum Parsimony
- NCBI GEO / GSE43867
- Differential-expression analysis
- Benjamini-Hochberg multiple-testing correction
- TargetScan
- UniProtKB
- NCBI Protein

---

## Skills Demonstrated

- Comparative protein sequence analysis
- Multiple-sequence alignment
- Phylogenetic tree reconstruction
- Evolutionary interpretation
- Gene-expression data analysis
- Statistical hypothesis testing
- Multiple-testing correction
- miRNA differential-expression analysis
- Biological database integration
- miRNA target-prediction interpretation
- Reproducible bioinformatics analysis

---

## Project Details

See **[results.md](./results.md)** for complete results, figures, phylogenetic-tree interpretation, differential-expression analysis, comparison with the published study, and project limitations.

---

## References

- Wei S, Wang Y, Xu H, Kuang Y. *Screening of potential biomarkers for chemoresistant ovarian carcinoma with miRNA expression profiling data by bioinformatics approach.* Oncology Letters. 2015;10:2427–2431.
- NCBI GEO accession: GSE43867
- UniProtKB
- TargetScanHuman
