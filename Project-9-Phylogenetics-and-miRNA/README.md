# Project 9 - TPI Phylogenetics and Ovarian-Cancer miRNA Reanalysis

## Overview

This project modernizes a 2021 bioinformatics assignment by rebuilding both analyses as a reproducible portfolio project:

1. phylogenetic comparison of triosephosphate isomerase (TPI) proteins from eight organisms using UPGMA and maximum parsimony; and
2. differential-expression reanalysis of the GSE43867 ovarian-cancer chemotherapy-response miRNA dataset, followed by a documented target-prediction comparison.

The repository includes source data, accession metadata, reusable Python scripts, complete tables, publication-quality figures, Newick trees, and an interpretation of differences between the new analysis, the old GEO2R screenshots, and the 2015 article.

## Key findings

- Human TPI clustered most closely with rabbit and then mouse in both phylogenetic approaches.
- *Dickeya/Musicola paradisiaca* Ech703 clustered with *Salmonella enterica*.
- GSE43867 contains 48 chemotherapy responders and 38 non-responders.
- Three miRNAs met the historical nominal rule (`P < 0.05`, `|logFC| > 1`): hsa-miR-592, hsa-miR-642, and hsa-miR-483-5p.
- None remained significant after Benjamini-Hochberg correction, so the miRNA findings are exploratory.
- The old TargetScan 7.2 result linked miR-483-5p to MAPK3, one of the genes emphasized in the original article. Current TargetScan 8.0 defaults do not provide exact family rows for the three detected mature miRNAs.

## Data and sequence selection

TPI proteins were retrieved from UniProtKB or NCBI Protein. Reviewed records were preferred. Cytosolic *Arabidopsis thaliana* TPI (P48491) was selected rather than the chloroplast isoform to make the subcellular comparison consistent. The Ech703 record is currently listed as *Musicola paradisiaca*, with *Dickeya paradisiaca* retained as a synonym.

GSE43867 was obtained from NCBI GEO. The analysis uses the submitter-normalized `VALUE` field in the family SOFT file. Complete and partial responses form the responder group; stable disease and no response form the non-responder group.

## Methods

### Phylogenetics

The script performs global pairwise Needleman-Wunsch alignment against the human reference, reconciles insertion columns into a shared alignment, calculates pairwise amino-acid p-distances, and builds a UPGMA tree. Maximum parsimony is evaluated with Fitch scoring across all 10,395 possible unrooted binary trees for eight taxa.

### Differential expression

For each of the 671 platform probes, the script calculates responder-minus-non-responder log fold change and a two-sided equal-variance t test. Benjamini-Hochberg adjusted P-values are also reported. The historical paper cutoff is retained for comparison, while the multiple-testing result is reported separately.

## Reproduction

```bash
python -m pip install -r requirements.txt
python scripts/phylogenetic_analysis.py
python scripts/differential_expression.py
```

The project itself is already populated with the generated results; running the scripts is optional.

## Interpretation
See [RESULTS.md](RESULTS.md) for figures, captions, numerical results, comparison with the original publication, and limitations.

## References

- Wei S, Wang Y, Xu H, Kuang Y. Screening of potential biomarkers for chemoresistant ovarian carcinoma with miRNA expression profiling data by bioinformatics approach. *Oncology Letters*. 2015;10:2427-2431. https://doi.org/10.3892/ol.2015.3610
- NCBI GEO accession GSE43867: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE43867
- UniProtKB: https://www.uniprot.org/
- TargetScanHuman 8.0: https://www.targetscan.org/vert_80/
- MEGA software: https://www.megasoftware.net/

