#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Function used in docking-based virtual screening with smina
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import pandas as pd
from rdkit import Chem
sys.path.append('..')
from utils.compound_preprocessing import smiles_to_mol_3D


def prepare_ligands(path_data, path_docking, fname_ligand_set):
    '''
    transfor and split the *.sdf to *m.pdbqt

    Parameters
    ----------
    path_data : string
        the path of the data
    path_docking : string
        the path for docking
    fname_ligand_set : string
        The file name of the ligands file

    Returns
    -------
    None
    '''

    # initialization of the lignads folder.
    if Path.exists(path_docking / 'ligands'):
        shutil.rmtree(path_docking, 'ligands')
    Path.mkdir(path_docking / 'ligands')

    # generate 3D coordinates
    df = pd.read_csv(path_data / (fname_ligand_set + '.csv'), sep=';')
    df['Mol3D'] = df['Smiles'].apply(smiles_to_mol_3D)

    w = Chem.SDWriter(str(path_docking / (fname_ligand_set + '_3D.sdf')))
    for mol_3D in df.Mol3D:
        w.write(mol_3D)
    w.close()

    # convert and split the SDF file into PDBQT files.
    subprocess.call('obabel %s -O %s/ligand.pdbqt -m' %
                    (path_docking /
                     (fname_ligand_set + '_3D.sdf'), path_docking / 'ligands'),
                    shell=True,
                    executable='/bin/bash')

    # rename the ligands according to their Name
    ligand_name_list = df['Name'].tolist()

    for i in range(len(ligand_name_list)):
        oldname = path_docking / 'ligands' / ('ligand%i.pdbqt' % (i + 1))
        newname = path_docking / 'ligands' / (ligand_name_list[i] + '.pdbqt')
        os.rename(oldname, newname)


def prepare_receptor(path_home, path_receptor, path_docking, fname_receptor):
    '''
    Split and transfor each Mpro structure to apo receptor and crystal ligand
    with PDBQT format.

    Parameters
    ----------
    path_receptor : string
        the path of the Mpro structures
    path_docking : string
        the path for docking
    fname_receptor : string
        The file name of each receptor file

    Returns
    -------
    None
    '''

    # move the Mpro structure to the docking path.
    shutil.copyfile(path_receptor / fname_receptor,
                    path_docking / 'receptor.pdb')
    # Split and convert each Mpro structure to apo receptor and crystal ligand.
    subprocess.call('pymol -c receptor_prepare.pml -Q',
                    shell=True,
                    executable='/bin/bash')
    # convert the apo receptor and crystal ligand from PDB to PDBQT format.
    subprocess.call('obabel %s/receptor_h.pdb -xr -O %s/receptor_h.pdbqt' %
                    (path_docking, path_docking),
                    shell=True,
                    executable='/bin/bash')
    subprocess.call('obabel %s/crystal_ligand.pdb -O %s/crystal_ligand.pdbqt' %
                    (path_docking, path_docking),
                    shell=True,
                    executable='/bin/bash')


def molecular_docking(path_docking, receptor_name):
    '''
    Docking the receptor_h.pdbqt in docking path with the ligands.

    Parameters
    ----------
    path_docking : string
        the path for docking

    Returns
    -------
    docking_score_receptor_ligands : list
        the list of the top docking score for each ligand to one receptor.
        list: [receptor, ligand, docking score]
    '''

    ligand_list = os.listdir(path_docking / 'ligands')
    docking_score_receptor_ligands = []

    # docking for every compounds in dataset to the receptor.
    for ligand in ligand_list:
        # for ligand in ['Amprenavir.pdbqt']:        # ketp for debuging
        docking_results = path_docking / 'poses' / (receptor_name + '_' +
                                                    ligand)

        subprocess.call("echo '--------docking for %s and %s--------'" %
                        (receptor_name, ligand.rstrip('.pdbqt')),
                        shell=True,
                        executable='/bin/bash')

        # docking process.
        # for more parameter, see 'smina --help'.
        subprocess.call('smina -r %s/receptor_h.pdbqt -l %s -o %s \
            --autobox_ligand %s/crystal_ligand.pdbqt \
                --autobox_add 8 --exhaustiveness 16' %
                        (path_docking, path_docking / 'ligands' / ligand,
                         docking_results, path_docking),
                        shell=True,
                        executable='/bin/bash')

        # collect the docking scores
        if Path.exists(docking_results) and (os.path.getsize(docking_results)
                                             != 0):
            scores_str = subprocess.check_output(
                "grep \"minimizedAffinity\" %s |head -n1|awk \'{print $3}\'" %
                docking_results,
                shell=True,
                executable='/bin/bash')
            scores_float = float(scores_str)
        else:
            scores_float = 0.0
        docking_score_receptor_ligands.append(
            [receptor_name,
             ligand.rstrip('.pdbqt'), scores_float])

    return docking_score_receptor_ligands
