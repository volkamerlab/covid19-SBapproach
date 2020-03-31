# COVID-19 main protease: Docking-based virtual screening workflow
This folder serves a workflow for docking-based virtual screening with the free software, smina.

## Background
To contribute to the global effort to combat COVID-19, [Diamond Light Source's XChem team](https://www.diamond.ac.uk/Instruments/Mx/Fragment-Screening.html) has been able to solve a new structure of the SARS-CoV-2 main protease (MPro) at high resolution (PDB ID: 6YB7), and complete a large XChem crystallographic fragment screen against it.

For more detials: https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem.html

We try to collect the existing protease inhibitors and docking them to the [Mpro with non-covalent hits complexes](https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem/Downloads.html), then rank the average docking for each ligand with all of the Mpro stuctures. Finally, 20 compounds will be selected as hit compounds for further study.

## Workflow

### Preparing for the ligands
    [Done] Read the compounds in dataset with CSV format and convert them to SDF format.
    [Done] Convert and split the dataset with SDF format to PDBQT  format after adding hydrogens.

### Preparing for all of the receptor
    [Done] Remove water.
    [Done] Remove DMS buffer.
    [Done] Add hydrogens.
    [Done] Extract the crystal_ligand(LIG).
    [Done] Save the apo protein and the crystal_ligand respectively and convert both of them to PDBQT format.

### Docking process
    [Done] Docking each compound from the dataset to all of the Mpro structures by smina.

### Scoring and ranking
    [Done] Collect the ligand pose with top docking score for each compound in each receptor, then calculate the average docking score for each compound to Mpros.
    [Done] Rank the compounds with the average docking score.
    [Done] Select top 20 compounds as hit compounds for further study.

## Exmaple
### Requirements
* [pandas](http://pandas.pydata.org/)
* [RDKit](https://www.rdkit.org)
* [smina](https://sourceforge.net/projects/smina/)
* [pymol](https://pymol.org/2/)
* [OpenBabel](http://openbabel.org/wiki/Main_Page)

### Quick start
#### Compounds dataset
Collect the Compounds as dataset with CSV format and put it in the data folder.

For example:
```
Name;Smiles
Saquinavir;CC(C)(C)NC(=O)[C@@H]1C[C@@H]2CCCC[C@@H]2CN1C[C@H]([C@H](CC3=CC=CC=C3)NC(=O)[C@H](CC(=O)N)NC(=O)C4=NC5=CC=CC=C5C=C4)O
Lopinavir;CC1=C(C(=CC=C1)C)OCC(=O)N[C@@H](CC2=CC=CC=C2)[C@H](C[C@H](CC3=CC=CC=C3)NC(=O)[C@H](C(C)C)N4CCCNC4=O)O
```

#### Docking process
```
python DockingScreeningRun.py ../../data/proteaseFDAdrugs.csv
```
Tip: Running the process on the cluster is a good idea.
#### Analyze
```
jupyter notebook DockingScreeningAnalyse.ipynb
```
