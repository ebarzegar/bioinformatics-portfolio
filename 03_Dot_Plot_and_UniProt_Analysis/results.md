# Results

## 1. Comparative Dot Plot Analysis Using EMBOSS Dotmatcher

The objective of this analysis was to compare the nucleotide sequences of the human **TPI1** gene and the rabbit **TPI1** gene using the EMBOSS Dotmatcher tool. Dot plot analysis allows visualization of regions of sequence similarity and conservation between two sequences.

## Method

The nucleotide sequences of human and rabbit **TPI1** were analyzed using EMBOSS Dotmatcher.

**Parameters used**

- Window size: 5
- Threshold: 10

## Results
<img width="1028" height="787" alt="figure1_human_mouse_dotplot png" src="https://github.com/user-attachments/assets/d8fc32b4-8c7d-46bf-8ef2-738e3f66cfee" />

Dot plot comparison of the coding sequences (CDS) of human and mouse **TPI1** generated using EMBOSS Dotmatcher.
The dot plot reveals regions of sequence similarity between the human and mouse **TPI1** coding sequences. Conserved regions appear as diagonal alignments, indicating that the coding sequence has remained highly conserved during evolution. Small interruptions or deviations from the diagonal reflect nucleotide substitutions or minor sequence differences between the two species. Overall, the analysis demonstrates the strong evolutionary conservation of the TPI1 gene, consistent with its essential role in glycolysis.

---

## 2. Self Dot Plot Analysis Using UGENE

## Objective

The objective of this analysis was to identify repeated regions within the human TPI1 protein sequence by generating a self-dot plot using UGENE.

## Method

The amino acid sequence of the human TPI1 protein was analyzed against itself using the UGENE Dot Plot tool.

**Parameters**

- Minimum repeat length: 5
- Repeat identity: 80%

## Results
<img width="815" height="520" alt="figure2_self_dotplot_ugene png" src="https://github.com/user-attachments/assets/073a322a-4146-4dac-a79e-43ab92aeb915" />

Self-dot plot of the human TPI1 protein generated using UGENE.
## Interpretation

The main diagonal represents the perfect alignment of the protein sequence with itself.
Short off-diagonal lines indicate small repeated or locally similar sequence regions within the TPI1 protein. 
No large duplicated regions were observed, suggesting that the protein does not contain extensive internal repeats.

---

## 3. Protein Annotation Using UniProtKB
The human TPI1 protein was explored using the UniProtKB database to investigate its biological function, post-translational modifications, structural features, and Gene Ontology (GO) annotations.

### 3.1 Gene Ontology
Gene Ontology (GO) provides standardized descriptions of a protein's molecular function, the biological processes in which it participates, and its cellular localization.

### Results
<img width="1432" height="450" alt="gene_ontology png" src="https://github.com/user-attachments/assets/e7f28765-c43d-45ba-818c-f6c9f4ac24bb" />

https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=P60174
Gene Ontology annotations of human TPI1 obtained from UniProtKB.

## Interpretation

The GO annotations indicate that TPI1 functions primarily as a triose-phosphate isomerase involved in glycolysis and gluconeogenesis. The protein is mainly localized in the cytosol, consistent with its role in cellular energy metabolism.

---

## 3.2 Post-translational Modifications (PTMs)

Post-translational modifications (PTMs) are chemical changes that occur after protein synthesis and can influence protein activity, localization, or interactions.

### Results

<img width="1457" height="342" alt="ptms png" src="https://github.com/user-attachments/assets/6f7b9e6e-b884-4448-a3bc-ecaab46c7bb8" />


Post-translational modifications reported for human TPI1 in UniProtKB.

### Interpretation

UniProtKB reports several experimentally supported or predicted post-translational modifications for TPI1, including modified amino acid residues. These modifications may contribute to the regulation of protein function under specific biological conditions.

---

## 3.3 Disulfide Bonds

Disulfide bonds stabilize the three-dimensional structure of many extracellular proteins.

### Results

No disulfide bonds were reported for human TPI1 in UniProtKB.

### Interpretation

The absence of disulfide bonds is consistent with TPI1 being a soluble cytosolic enzyme rather than a secreted protein. Cytosolic proteins are typically found in a reducing environment where stable disulfide bonds rarely form.

---

## 3.4 Three-dimensional Protein Structure

The three-dimensional structure of TPI1 was examined using the structural information available through UniProtKB.

### Results
<img width="437" height="443" alt="3d_structure png" src="https://github.com/user-attachments/assets/448554dd-63a4-4b61-9a52-38ec0e16a0e6" />


Three-dimensional structure of the human TPI1 protein.

### Interpretation

The three-dimensional structure demonstrates the compact folding of TPI1 that is characteristic of enzymes involved in central metabolism. Structural visualization provides insight into the spatial organization required for catalytic activity and substrate binding.
