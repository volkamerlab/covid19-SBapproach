#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The __main__ script for docking-based virtual screening with smina
"""

import sys
from pathlib import Path
import shutil
import tarfile
import pandas as pd
from docking_screening import prepare_ligands
from docking_screening import prepare_receptor
from docking_screening import molecular_docking

# initialization and set docking and docking_results path
path_home = Path.cwd()
path_data = path_home / '..' / '..' / 'data'

if Path.exists(path_data / 'docking'):
    shutil.rmtree(path_data / 'docking')
if not Path.exists(path_data / 'docking_results'):
    Path.mkdir(path_data / 'docking_results')
Path.mkdir(path_data / 'docking')
Path.mkdir(path_data / 'docking' / 'poses')

path_docking = path_data / 'docking'
path_docking_results = path_data / 'docking_results'

# set the path of receptors, it must be in the data path.
# The receptors are PDB format.
path_receptor = path_data / 'diamond_xchem_screen_mpro_all_pdbs'
# get the name of ligands dataset, it must be in the data path.
# the ligands dataset is the CSV format with 'Name;Smiles' as head.

fname_ligand_set = Path(sys.argv[1]).stem
# fname_ligand_set = 'proteaseFDAdrugs'  # kept for debuging
# prepare for the ligands.
prepare_ligands(path_data, path_docking, fname_ligand_set)

# docking for all of the receptor.
with open(path_receptor /
          'diamond_xchem_screen_mpro_non_covalent_pdbs.dat') as f:
    receptor_list = f.readlines()
    for i in range(len(receptor_list)):
        receptor_list[i] = receptor_list[i].rstrip('\n')

results_all = []

for fname_receptor in receptor_list:
    # for fname_receptor in ['Mpro-x0354.pdb']:      # kept for debuging
    # prepare for receptor.
    prepare_receptor(path_home, path_receptor, path_docking, fname_receptor)
    # docking with smina and collect the results.
    results_all.append(
        molecular_docking(path_docking, fname_receptor.rstrip('.pdb')))

print(results_all)

# save the result.
index = []
columns = []
score = list(results_all)

for i in range(len(results_all)):
    index.append(results_all[i][0][0])
for j in range(len(results_all[0])):
    columns.append(results_all[0][j][1])
for i in range(len(index)):
    for j in range(len(columns)):
        score[i][j] = results_all[i][j][2]

results_tmp_pd = pd.DataFrame(score, index=index, columns=columns).T
results_tmp_pd.to_csv(path_docking_results /
                      ('%s_docking_results.csv' % fname_ligand_set))

# zip the pose results
with tarfile.open(
        path_docking_results / ('%s_poses.tar.bz2' % fname_ligand_set),
        'w:bz2') as tar:
    tar.add(path_docking / 'poses', arcname='%s_poses' % fname_ligand_set)

# clean the temporary materials
shutil.rmtree(path_docking)
