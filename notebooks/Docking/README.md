# COVID-19 main protease: Docking-based virtual screening workflow
This repo serves a workflow for docking-based virtual screening with the free software, smina.

## Background
To contribute to the global effort to combat COVID-19, [Diamond Light Source's XChem team](https://www.diamond.ac.uk/Instruments/Mx/Fragment-Screening.html) has been able to solve a new structure of the SARS-CoV-2 main protease (MPro) at high resolution (PDB ID: 6YB7), and complete a large XChem crystallographic fragment screen against it. 

For more detials: https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem.html

We try to collect the existing protease inhibitors and docking them to the [Mpro with non-covalent hits complexes](https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem/Downloads.html), then rank the average docking for each ligand with all of the Mpro stuctures. Finally, 5~8 compounds will be selected as hit compounds for further study. 

## Workflow

### Preparing for the ligands
    [] Translate and split the file *.sdf to *n.pdbqt after adding hydrogens. 

### Preparing for all of the receptor
    [] Remove water.
    [] Remove DMS buffer.
    [] Add hydrogens.
    [] Extract the crystal_ligand(LIG).
    [] Save the apo protein and the crystal_ligand respectively as PDBQT format.

### Docking process
    [] Docking each compound to all of the receptor structures by smina.

### Scoring and ranking
    [] Collect the ligand pose with top docking score for each compound in each receptor, then calculate the average docking score for each compound to Mpros. 
    [] Rank the compounds with the average docking score.
    [] Select top N compounds as hit compounds for further study.

 