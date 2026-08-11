# Results

## 1. TPI phylogenetic analysis

Eight TPI amino-acid sequences were aligned into 280 columns. The shortest mammalian distances were human-rabbit (0.0161 substitutions per compared site), followed by mouse. The two Gram-negative bacteria, *Dickeya/Musicola paradisiaca* Ech703 and *Salmonella enterica*, clustered together. *Staphylococcus aureus*, a Gram-positive bacterium, was the most distant branch in the UPGMA reconstruction.
<img width="1980" height="1210" alt="TPI_UPGMA_tree" src="https://github.com/user-attachments/assets/7aa6badb-2030-4f50-8197-6ff561450b43" />
UPGMA tree based on pairwise amino-acid p-distances calculated from the TPI alignment.

An exhaustive maximum-parsimony search evaluated all 10,395 unrooted binary topologies for eight taxa. The best score was 452 amino-acid state changes. Human and rabbit were sister taxa, mouse joined the mammalian group, and *Dickeya* and *Salmonella* were sister taxa.

<img width="1980" height="1210" alt="TPI_parsimony_tree" src="https://github.com/user-attachments/assets/93e62aa5-244d-4973-857c-2c125d62987c" />

Best maximum-parsimony topology. Branch lengths are not proportional to evolutionary distance.

Both approaches recover the strongest biologically expected relationships. Deeper branching differs slightly because UPGMA assumes an approximately constant evolutionary rate, whereas maximum parsimony minimizes the total number of character changes.

## 2. GSE43867 miRNA analysis

The dataset contains 86 chemotherapy-treated serous epithelial ovarian carcinomas: 48 responders (36 complete and 12 partial response) and 38 non-responders (10 stable disease and 28 no response). All 671 platform probes were tested using the submitter-normalized values.

Using the historical screening rule, `P < 0.05` and `|logFC| > 1`, three miRNAs were detected:

| miRNA | logFC (responder - non-responder) | P-value | BH-adjusted P-value |
|---|---:|---:|---:|
| hsa-miR-592 | 1.390 | 0.0022 | 0.648 |
| hsa-miR-642 | -1.020 | 0.0090 | 0.648 |
| hsa-miR-483-5p | -1.355 | 0.0160 | 0.648 |

No probe remained significant at BH-FDR < 0.05. These should therefore be described as exploratory candidates under the historical nominal cutoff, not independently confirmed biomarkers.
<img width="1760" height="1320" alt="miRNA_volcano_plot" src="https://github.com/user-attachments/assets/ec40e84f-1e3d-416b-8198-ad7ac2e8e9ee" />

Volcano plot of all 671 probes. Red points meet the historical nominal cutoff.

<img width="2640" height="1540" alt="miRNA_heatmap_top20" src="https://github.com/user-attachments/assets/6feceba7-73b4-4f5e-8e10-8555fa39ebaf" />
Row-standardized expression of the 20 probes with the smallest nominal P-values.

<img width="2772" height="1056" alt="selected_miRNA_expression" src="https://github.com/user-attachments/assets/03c4beb6-786f-4b29-bbc0-d706c38a0a42" />
Submitter-normalized expression distributions for the three historical-cutoff candidates.

## 3. Comparison with the 2015 paper and old answer

Wei et al. reported six miRNAs: miR-760, miR-483-5p, miR-766, miR-198, miR-129-3p and miR-642. The old GEO2R screenshot also displayed miR-592 near the top, but the paper did not include it in its six-miRNA table. This reanalysis confirms that the public submitter-normalized values and the publication table are not perfectly concordant.

Possible reasons include differences in the exact statistical model, probe filtering, GEO2R/Bioconductor versions, preprocessing, or undocumented selection decisions. The repository preserves the calculated output rather than forcing it to match the paper.

## 4. Downstream target comparison

The original answer used TargetScanHuman 7.2 for miR-483-5p and miR-642-3p. MAPK3 appeared among the visible miR-483-5p predictions and was also one of the key genes discussed by Wei et al., providing a direct link between the old target-prediction step and the article's downstream network interpretation.

TargetScanHuman is now release 8.0. Its current default-prediction download did not contain exact human family rows for miR-592, miR-642, or miR-483-5p; rows for miR-483-3p are a different mature arm and were not incorrectly substituted. Consequently, the legacy predictions are retained as historical results and clearly labelled rather than represented as current predictions.

## Limitations

- The differential-expression test reproduces the public normalized matrix with a classical two-group t test; GEO2R uses limma's moderated statistics, so exact P-values can differ.
- Nominal P-values do not survive correction across 671 probes.
- Target predictions are hypotheses and require experimental validation.
- Eight proteins provide a teaching-scale phylogeny, not a species-tree reconstruction.

