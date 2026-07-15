# Project 5: Molecular Docking and Protein Modeling

## Project Overview

This project explores how computational molecular docking can be used to investigate protein–ligand interactions. Using SwissDock, I reproduced part of a published COVID-19 study that examined the interaction between melatonin and the SARS-CoV-2 main protease (Mpro). The predicted docking pose was then compared with the interaction reported in the research article.

Rather than attempting to prove that melatonin is an effective treatment, this project demonstrates how molecular docking can be used to computationally predict whether a small molecule is capable of binding to a target protein and to estimate its preferred binding orientation.

---

## Biological Background

### Target Protein

The target protein selected for this project is the **SARS-CoV-2 Main Protease (Mpro)**, also known as the **3CL protease**.

This viral enzyme plays an essential role in the replication of SARS-CoV-2 by cleaving viral polyproteins into functional proteins required for the viral life cycle. Because viral replication depends on the activity of Mpro, it has become one of the primary targets for antiviral drug discovery.

### Ligand

The ligand investigated in this project is **melatonin**.

Although melatonin is widely recognized as the hormone responsible for regulating the sleep–wake cycle, it also possesses antioxidant and anti-inflammatory properties. During the COVID-19 pandemic, researchers investigated whether melatonin might also interact directly with viral proteins, including the SARS-CoV-2 main protease.

---

## What is Molecular Docking?

Molecular docking is a computational technique used to predict how a small molecule (ligand) interacts with a protein.

A useful analogy is to imagine:

- the **protein** as a lock,
- the **ligand** as a key.

SwissDock evaluates thousands of possible orientations of the ligand inside the protein's binding pocket and estimates which configuration is the most energetically favorable.

Importantly, molecular docking **does not prove** that a compound is an effective drug. Instead, it provides computational predictions that help researchers identify promising candidates for future laboratory experiments.

---

## Objectives

- Reproduce a published molecular docking study.
- Investigate the interaction between melatonin and SARS-CoV-2 Mpro.
- Compare computational docking results with published findings.
- Gain practical experience using molecular docking software and interpreting protein–ligand interactions.

---

## Tools Used

- SwissDock
- Protein Data Bank (PDB)
- Published literature

---
## Reference paper:
[Feitosa_et_al_2020_Melatonin_Mpro.pdf.pdf](https://github.com/user-attachments/files/30055825/Feitosa_et_al_2020_Melatonin_Mpro.pdf.pdf)

