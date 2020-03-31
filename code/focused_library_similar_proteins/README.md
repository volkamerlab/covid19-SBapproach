# COVID-19 main protease: Ligands from similar binding sites

Read across the PDB to find similar binding sites and their associated molecules in ChEMBL.

## Steps

### Target and binding site definition

1. [Done] Decide on a target.
   - COVID-19 main protease
   
2. [Done] Decide on structure.
   - [6LU7](http://www.rcsb.org/structure/6LU7)
   - In complex with fragments from [Diamond's XChem fragment screen](https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem.html)
   
   Diamond's XChem fragment screen structures live in `data/diamond_xchem_screen_mpro_all_pdbs`.

3. [Done] Define binding site residues.
   - Load all XChem structures (`biopython`).
   - Get residues in a defined radius of ligand centroids.
   - Find overlapping residues across all structures (define residue coverage threshold).
   
   Check out notebook `notebooks/01_binding_site_definition.ipynb`.

### Similar binding sites / proteins

4. [Done] Submit job to ProBis, including binding site definition.
   - Full 6LU7: [ProBis job URL](http://probis.cmm.ki.si/?what=job&job_id=24032003478165)
   - Binding site only:  
   
     | # residues | distance cutoff | coverage cutoff | ProBis job URL                                                            |
     |------------|-----------------|-----------------|---------------------------------------------------------------------------|
     | 68         | 15              | 0.5             | [ProBis job URL](http://probis.cmm.ki.si/?what=job&job_id=25032048431709) |

5. [Done] Download ProBis results.
   - *ProBis protein table*: "Similar Proteins" tab > "Download Table"
   - *ProBis ligand table*: "Predicted Ligands" tab > "Download Table"
   
   ProBis results live in `data/focused_library_similar_proteins/probis`.
   
6. [Done] Parse ProBis ligand and protein tables.

   Check out notebook `notebooks/02_probis_data_preparation.ipynb`.

### Active molecules against similar proteins

7. [Done] Query ChEMBL for "active" molecules, given a defined pIC50 cutoff (`chembl_webresource_client`).
   
   - Get molecule and bioactivity data for proteins from *ProBis protein table* (by UniProt IDs).
   - Filter ChEMBL molecules by bioactivity (define threshold) to keep only “active” molecules.

   Checkout notebooks:
   - Pipeline (to obtain molecule library) `notebooks/03_chembl_molecules_from_uniprot_ids.ipynb`.
   - Result (molecule library) `notebooks/04_molecule_library.ipynb`.
   
8. ProBis offers also prediced ligands (*ProBis ligand table*).
   - Find out how this dataset can be of use here.
   - Get molecule and bioactivity data for ligands from *ProBis ligand table* by ligand name?


## Notebooks


### Pipeline

1. Binding site definition
   - Define target's binding site based on multiple ligand positions.
   - Notebook: `notebooks/01_binding_site_definition.ipynb`
2. Binding site comparison
   - Download results from ProBis (manually) and parse files
   - Get UniProt IDs from most similar proteins
   - Notebook: `notebooks/02_probis_data_preparation.ipynb`
3. Molecules active against similar proteins
   - Get active molecules against similar proteins based on UniProt IDs (ChEMBL query)
   - Notebook: `notebooks/03_chembl_molecules_from_uniprot_ids.ipynb`
4. Explore molecule library
   - Look at output molecule library
   - Notebook: `notebooks/04_molecule_library.ipynb`
   
   
### Example data

Pipeline at the example of:

- Pocket comparison only (15 A radius around ligand with 50% coverage across structures)
- Data: `data/probis/probis_pocket_15_0.5`
- [ProBis job URL](http://probis.cmm.ki.si/?what=job&job_id=25032048431709)



