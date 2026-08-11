# Results

## 1. TPI Phylogenetic Analysis

Eight TPI amino-acid sequences were aligned into 280 columns. The shortest mammalian distance was observed between human and rabbit TPI (0.0161 substitutions per compared site), with mouse also clustering within the mammalian group. The two Gram-negative bacteria, *Dickeya/Musicola paradisiaca* Ech703 and *Salmonella enterica*, clustered together. *Staphylococcus aureus*, a Gram-positive bacterium, formed the most distant branch in the UPGMA reconstruction.

### UPGMA Phylogeny

The UPGMA tree was constructed from pairwise amino-acid p-distances calculated from the TPI alignment.

![UPGMA phylogenetic tree of TPI proteins](results/TPI_UPGMA_tree.png)

**Figure 1. UPGMA phylogenetic tree of TPI proteins.** Human and rabbit TPI show the closest relationship, with mouse joining the mammalian cluster. *Dickeya/Musicola paradisiaca* Ech703 and *Salmonella enterica* also cluster together, reflecting their relatively similar TPI sequences.

### Maximum-Parsimony Phylogeny

An exhaustive Maximum-Parsimony search evaluated all 10,395 possible unrooted binary topologies for eight taxa. The best topology had a parsimony score of **452 amino-acid state changes**.

Human and rabbit were recovered as sister taxa, with mouse joining the mammalian group. *Dickeya/Musicola paradisiaca* Ech703 and *Salmonella enterica* were also recovered as sister taxa.

![Maximum-Parsimony phylogenetic tree of TPI proteins](results/TPI_parsimony_tree.png)

**Figure 2. Maximum-Parsimony phylogenetic tree of TPI proteins.** The tree represents the topology requiring the minimum number of amino-acid state changes. Branch lengths are not proportional to evolutionary distance.

### Interpretation

Both phylogenetic approaches recovered the strongest biologically expected relationships, particularly the clustering of the three mammalian TPI proteins and the close relationship between *Dickeya/Musicola paradisiaca* and *Salmonella enterica*.

Some deeper relationships differ between the two trees because the methods use different assumptions. UPGMA groups sequences according to pairwise evolutionary distance and assumes an approximately constant evolutionary rate, whereas Maximum Parsimony searches for the topology requiring the smallest total number of character-state changes.

---

## 2. GSE43867 miRNA Differential-Expression Analysis

The GSE43867 dataset contains **86 chemotherapy-treated serous epithelial ovarian carcinoma samples**, consisting of:

- **48 responders:** 36 complete responses and 12 partial responses
- **38 non-responders:** 10 stable-disease samples and 28 no-response samples

All **671 platform probes** were tested using the submitter-normalized expression values.

Using the screening criteria `P < 0.05` and `|logFC| > 1`, three miRNAs were identified:

| miRNA | logFC (responder − non-responder) | P-value | BH-adjusted P-value |
|---|---:|---:|---:|
| hsa-miR-592 | 1.390 | 0.0022 | 0.648 |
| hsa-miR-642 | -1.020 | 0.0090 | 0.648 |
| hsa-miR-483-5p | -1.355 | 0.0160 | 0.648 |

Positive logFC indicates higher expression in responders, whereas negative logFC indicates lower expression in responders. Therefore, **hsa-miR-592 was higher in responders**, while **hsa-miR-642 and hsa-miR-483-5p were lower in responders**.

No probe remained significant at **BH-FDR < 0.05** after correction for multiple testing. The three miRNAs should therefore be interpreted as **exploratory candidates identified under the nominal screening criteria rather than independently confirmed biomarkers**.

### Differential-Expression Visualization

![Volcano plot of GSE43867 miRNA differential expression](results/miRNA_volcano_plot.png)

**Figure 3. Volcano plot of miRNA differential expression.** All 671 probes are shown according to responder-versus-non-responder log fold change and statistical significance. Highlighted points represent miRNAs meeting the nominal criteria of `P < 0.05` and `|logFC| > 1`.

### Expression Patterns

Expression patterns of the most variable or differentially expressed miRNAs were further visualized using a heatmap, while the three selected candidates were examined directly across responder and non-responder samples.

![Heatmap of miRNA expression](results/miRNA_heatmap_top20.png)

**Figure 4. Heatmap of miRNA expression patterns.** Expression profiles illustrate variation among chemotherapy responders and non-responders across the selected miRNAs.

![Expression of selected miRNAs](results/selected_miRNA_expression.png)

**Figure 5. Expression of selected candidate miRNAs.** Expression distributions of hsa-miR-592, hsa-miR-642, and hsa-miR-483-5p are shown between chemotherapy responders and non-responders.

---

## 3. Comparison with the Published Study

Wei et al. reported six candidate miRNAs associated with chemotherapy response: **miR-760, miR-483-5p, miR-766, miR-198, miR-129-3p, and miR-642**.

The present analysis identified **miR-642 and miR-483-5p**, which overlap with the published candidate set, as well as **miR-592**, which was not included in the publication's final six-miRNA table.

The difference between the reproduced analysis and the published results may reflect differences in statistical methodology, probe filtering, preprocessing, software or package versions, or additional selection criteria used during the original analysis.

Rather than adjusting the analysis to reproduce the published candidate list, the results reported here preserve the output obtained from the stated dataset, sample classification, and statistical criteria.

---

## 4. Downstream miRNA Target Comparison

Target prediction was examined as a downstream analysis to investigate potential gene-level consequences of the identified miRNAs.

Previous TargetScanHuman 7.2 predictions for **miR-483-5p** included **MAPK3**, a gene also emphasized in the downstream network analysis reported by Wei et al. This provides a connection between the differentially expressed miRNA analysis and potential regulatory targets relevant to the published study.

TargetScanHuman has since been updated to release 8.0. The current default-prediction dataset did not provide exact human family rows corresponding to **miR-592, miR-642, or miR-483-5p**. Importantly, predictions for **miR-483-3p** were not substituted for miR-483-5p because the 3p and 5p products represent different mature miRNA strands and can have different target profiles.

The TargetScan 7.2 results are therefore retained as a documented target-prediction comparison rather than presented as newly generated TargetScan 8.0 predictions.

---

## Limitations

- Differential expression was calculated from the public normalized expression matrix using a classical two-group t test, whereas GEO2R uses limma moderated statistics; therefore, exact P-values may differ between approaches.
- None of the candidate miRNAs remained significant after multiple-testing correction across the 671 probes.
- Computational miRNA target predictions represent hypotheses and require experimental validation.
- Phylogenetic analysis of eight TPI proteins provides a focused comparative analysis rather than a comprehensive reconstruction of species evolution.
- UPGMA assumes approximately constant evolutionary rates among lineages, which may not hold across distantly related taxa.
