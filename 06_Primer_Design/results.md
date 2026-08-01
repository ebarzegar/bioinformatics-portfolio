
## 1. Identification of Homologous Sequences Using BLASTN

The human TPI1 nucleotide sequence was submitted to the NCBI BLASTN program. Homologous nucleotide sequences from other organisms were identified based on sequence similarity, query coverage, and E-value.

### Results
<img width="1512" height="730" alt="image" src="https://github.com/user-attachments/assets/c71fb72e-a501-4411-9172-25b14d2744a8" />

[seqdump.txt](https://github.com/user-attachments/files/30200558/seqdump.txt)# Primer Design and Specificity Analysis
BLASTN results showing homologous TPI1 nucleotide sequences identified in different organisms.
### Interpretation
BLASTN results showing homologous TPI1 nucleotide sequences identified in different organisms.
The BLASTN search identified highly similar TPI1 sequences in multiple species, particularly among primates. The highest sequence similarity was observed in closely related organisms, while more distant species showed lower sequence identity. These results demonstrate that TPI1 is highly conserved during evolution, reflecting its essential role in cellular metabolism.

---

## 2. Protein Engineering

### Objective
To investigate reported amino acid variants and protein engineering studies associated with the human TPI1 protein.
### Method
The UniProtKB database was searched for experimentally reported variants and amino acid substitutions of human TPI1. Reported sequence changes and their annotations were examined.
### Results
<img width="1880" height="678" alt="Screenshot 2026-07-20 145140" src="https://github.com/user-attachments/assets/ffcf654b-8f37-410b-be25-5c0b190b3158" />
<img width="1480" height="453" alt="Screenshot 2026-07-20 145219" src="https://github.com/user-attachments/assets/1d0a4ccf-b77e-4dfa-89b9-66492a6d65f6" />


Reported amino acid variants of human TPI1 obtained from UniProtKB.
### Interpretation
The UniProt entry contains several reported amino acid substitutions in TPI1. These variants demonstrate how changes in the protein sequence can influence protein function or be associated with specific biological or clinical phenotypes. Studying naturally occurring and engineered variants helps researchers understand the relationship between protein sequence, structure, and function.

---

## 3. Primer Design and Specificity Analysis

### Objective

To design a primer pair for the human TPI1 transcript and evaluate its specificity using NCBI Primer-BLAST.

### Method

The human TPI1 transcript variant 2 (NCBI RefSeq: NM_001159287.1) was submitted to NCBI Primer-BLAST. Primer pairs were designed for a predicted PCR product between 100 and 300 bp, with an optimal primer melting temperature of approximately 60°C. Specificity was assessed against the human RefSeq mRNA database.

### Results

<img width="1788" height="552" alt="Screenshot 2026-07-20 151358" src="https://github.com/user-attachments/assets/03a4adca-e1be-460f-98d0-bfb2e5ed634e" />

Graphical positions of candidate primer pairs designed for the human TPI1 transcript using NCBI Primer-BLAST.

<img width="1693" height="392" alt="Screenshot 2026-07-20 151448" src="https://github.com/user-attachments/assets/871a18e1-662f-450f-ba4f-592ee99dcf56" />
Detailed Primer-BLAST results for the selected TPI1 primer pair.

### Selected Primer Pair

| Property | Forward primer | Reverse primer |
|---|---|---|
| Sequence (5′→3′) | ATATAAGTGGGCAGTGGCCG | CCAGTTTCCCCCAACGAAGA |
| Template strand | Plus | Minus |
| Length | 20 nt | 20 nt |
| Position | 83–102 | 186–167 |
| Melting temperature | 59.89°C | 59.89°C |
| GC content | 55.00% | 55.00% |
| Self-complementarity | 5.00 | 3.00 |
| Self 3′ complementarity | 3.00 | 0.00 |

**Predicted PCR product length:** 104 bp

**Specificity result:** The primer pair was specific to the input TPI1 transcript, with no additional targets identified in the selected human RefSeq mRNA database.

### Interpretation

The selected primers have identical melting temperatures and balanced GC contents, allowing them to anneal efficiently under the same PCR conditions. The low self-complementarity values, particularly at the 3′ ends, reduce the likelihood of primer-dimer formation. Primer-BLAST identified only the intended human TPI1 transcript in the selected database, supporting the specificity of the primer pair.

The primers do not begin at the TPI1 start codon because PCR primers do not need to amplify the entire coding sequence. Instead, they flank a short, specific region of the transcript and generate a 104-bp product.

---

## 4. Primer Design for Gene Expression Analysis

## Experimental Scenario

In this case study, the objective was to compare the expression of the mouse **Tpi1** gene between treated and untreated cells using PCR-based methods. Total RNA was extracted from both samples and converted into cDNA by reverse transcription. However, it was assumed that residual genomic DNA contamination remained in the RNA preparations.

To ensure that gene expression measurements reflected **mRNA-derived cDNA** rather than contaminating genomic DNA, different primer design strategies were developed for three experimental applications:

- Quantitative PCR (qPCR)
- Conventional PCR followed by agarose gel electrophoresis
- Probe-based quantitative PCR (qPCR)

The primers were designed using NCBI Primer-BLAST while considering exon–intron organization to minimize amplification of genomic DNA.

### 4.1 qPCR Primers

### Objective

To design exon-junction qPCR primers for the mouse **Tpi1** transcript that specifically amplify cDNA while minimizing amplification from contaminating genomic DNA.

### Method

The mouse **Tpi1** transcript (NCBI RefSeq: **NM_009415.3**) was submitted to **NCBI Primer-BLAST**. Primer design parameters were adjusted to generate a short qPCR amplicon (80–150 bp), and primers were required to span an exon-exon junction. Candidate primer pairs were evaluated according to product size, melting temperature (Tm), GC content, self-complementarity, and 3′ self-complementarity.

### Results

<img width="1802" height="566" alt="image" src="https://github.com/user-attachments/assets/39e83f23-2fa8-4d7b-9a81-e831a7814d56" />

Graphical representation of candidate qPCR primer pairs designed for the mouse **Tpi1** transcript.

<img width="1817" height="532" alt="image" src="https://github.com/user-attachments/assets/7b5d04ee-f946-43a7-825b-20bc2108226d" />

Detailed properties of the selected exon-junction primer pair.

### Selected Primer Pair

| Property | Forward Primer | Reverse Primer |
|-----------|----------------|----------------|
| Sequence (5′→3′) | ACTGGGGAAATCAGCCCTGG | CTAGGGCGTGGCTCACTTT |
| Length | 20 nt | 19 nt |
| Melting temperature (Tm) | 61.87°C | 59.70°C |
| GC content | 60.00% | 57.89% |
| Self-complementarity | 4.00 | 4.00 |
| 3′ self-complementarity | 3.00 | 0.00 |

**Predicted product size:** 130 bp

**Primer design strategy:** The forward primer spans the exon junction between exons 275 and 276.

### Interpretation

The selected primer pair generates a short 130 bp amplicon, making it suitable for quantitative PCR analysis. The forward primer spans an exon-exon junction, allowing efficient amplification of cDNA while minimizing amplification of contaminating genomic DNA. The primers have similar melting temperatures and balanced GC contents, supporting efficient amplification under the same PCR conditions. The low 3′ self-complementarity also reduces the likelihood of primer-dimer formation, making this primer pair appropriate for accurate measurement of **Tpi1** gene expression.

---

### 4.2 PCR and Agarose Gel Primers

### Objective

### Method

### Results

### Interpretation

---

### 4.3 qPCR Primers with Probe

### Objective

### Method

### Results

### Interpretation
