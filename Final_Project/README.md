# Final Project: Principal Component Analysis on a Torus

- The project report is uploaded [here](./Submission_v2.pdf). The appendix of this file contains the PDF-version of the Jupyter notebook
- The Jupyter notebook can be found [here](./Coding/0_Final_Notebook.ipynb), along with a [PDF version](./Coding/0_Final_Notebook.pdf)


## Abstract

In this project, we analyze a 500 ns alanine dipeptide simulation using PCA, dPCA, and torus-based dPCA+ to study its conformational dynamics from periodic dihedral angles $(\phi, \psi)$. While conventional PCA captures ~ 79% of variance, it introduces artifacts due to angular periodicity. dPCA improves this by sine-cosine transformation, and dPCA+ further preserves toroidal topology via maximal-gap shifting, producing more physically consistent free energy landscapes.

<div style="text-align: center;">
  <img src="./Coding/final_plots/png/free_energy_initial_hq.png" alt="Free Energy Landscape" width="350"/>
</div>
