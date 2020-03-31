# script for preparing the receptor.
# running by pymol.

# load the receptor structure
load ../../data/docking/receptor.pdb

# extract and save the ligand.
select ligand, resn LIG
save ../../data/docking/crystal_ligand.pdb, ligand

# remove the ligand, water, bufferadd, and add the hydrogens.
remove resn LIG
remove resn HOH
remove resn DMS
h_add elem O or elem N

# save the receptor.
save ../../data/docking/receptor_h.pdb
