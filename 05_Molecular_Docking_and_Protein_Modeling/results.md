# 1. Molecular Docking Using SwissDock

## Objective

To investigate the predicted interaction between melatonin and the SARS-CoV-2 main protease (Mpro) using molecular docking and compare the predicted binding pose with published findings.

---

## Method

The SARS-CoV-2 main protease (Mpro) and melatonin were selected based on the study by Feitosa et al. (2020). Molecular docking was performed using SwissDock, and the predicted protein–ligand interaction was compared with the docking result reported in the reference paper.

---

## Results
<img width="677" height="703" alt="SARS-CoV-2Structure" src="https://github.com/user-attachments/assets/b85f2689-36ab-498c-a26c-2ff1ac073718" />


Three-dimensional structure of the SARS-CoV-2 main protease (Mpro).

---
<img width="787" height="450" alt="SwissdockAlignment" src="https://github.com/user-attachments/assets/5a8a2432-b6ac-4111-a7ad-412d84d2dadc" />


Predicted binding pose of melatonin generated using SwissDock.

---
<img width="617" height="452" alt="reported Docking" src="https://github.com/user-attachments/assets/4d03057f-def4-4514-bb59-b34be861e55f" />


Docking interaction reported in Feitosa et al. (2020).

---

## Interpretation

The predicted docking pose placed melatonin within the binding region of the SARS-CoV-2 main protease. Comparison with the published docking result showed a similar binding location, demonstrating how molecular docking can be used to predict potential protein–ligand interactions. Although docking provides valuable computational insight, experimental validation is necessary to confirm biological activity.

## Reference

Feitosa EL, et al. (2020). *COVID-19: Rational discovery of the therapeutic potential of melatonin as a SARS-CoV-2 main protease inhibitor.* International Journal of Medical Sciences, 17(14), 2136–2148. https://doi.org/10.7150/ijms.48053

---
# 2. Protein–Protein Interaction Network

## Objective

To investigate the functional interaction network of human TPI1 using the STRING database and identify proteins that are closely associated with its biological function.
This analysis explores the protein interaction network of human TPI1 using STRING to identify proteins that are functionally associated with TPI1 and to better understand its role in cellular metabolism.

---

## Method

The human TPI1 protein was searched in the STRING database, and the predicted protein–protein interaction network was generated using the default parameters.

---

## Results
<img width="1428" height="721" alt="Protein–protein interactio" src="https://github.com/user-attachments/assets/4d0e1ea1-7dd1-45bc-81b1-1950b160f0bc" />

Protein–protein interaction network of human TPI1 generated using STRING.

---
## Interpretation

The STRING interaction network shows that TPI1 is functionally associated with several enzymes involved in glycolysis and central carbon metabolism. The dense connectivity within the network reflects the coordinated activity of metabolic enzymes required for efficient energy production. This analysis demonstrates that TPI1 functions as part of a larger biological system rather than as an isolated protein.

# 3. Protein Structure Prediction Using SWISS-MODEL

## Objective

To investigate the effect of a single amino acid substitution on the predicted three-dimensional structure of human TPI1 using SWISS-MODEL.

---

## Method

The amino acid sequence of human TPI1 was obtained from UniProt. A single amino acid substitution (K→A) was introduced into the sequence, and the modified protein sequence was submitted to SWISS-MODEL for comparative protein structure prediction.

---

## Results
<img width="1710" height="837" alt="The predicted model" src="https://github.com/user-attachments/assets/124c6c51-6696-4fa5-8014-cee0c5acd977" />

<img width="437" height="443" alt="3d_structure png" src="https://github.com/user-attachments/assets/f69de829-8b56-479c-b005-cdbf9fa1656b" />

 Predicted three-dimensional structure of the mutated human TPI1 generated using SWISS-MODEL vs. the original model.

---

## Interpretation

The predicted structure of the mutated TPI1 protein remained highly similar to the wild-type structure, indicating that this single amino acid substitution did not substantially alter the overall three-dimensional fold. This demonstrates an important concept in structural biology: individual amino acid substitutions do not necessarily cause major structural changes. However, even when the global structure is preserved, mutations may still influence protein stability, enzymatic activity, ligand binding, or interactions with other molecules. Therefore, computational structure prediction provides valuable insight, but experimental studies are required to determine the functional consequences of the mutation.
