"""
Functions for compound preprocessing
"""

from rdkit import Chem
from rdkit.Chem import AllChem


def generate_mol_3D(mol_2D):
    '''
    generate 3D conformations from mol_2D to mol_3D

    Parameters
    ----------
    mol_2D : rdkit.Chem.rdchem.Mol
        2D mol for compounds in dataset.

    Returns
    -------
    mol_3D : rdkit.Chem.rdchem.Mol
        3D mol for compounds in dataset.
    '''

    mol_3D = Chem.AddHs(mol_2D)
    AllChem.EmbedMolecule(mol_3D)
    AllChem.UFFOptimizeMolecule(mol_3D)
    return mol_3D


def smiles_to_mol_3D(smiles):
    '''
    generate 3D conformations from smiles to mol_3D

    Parameters
    ----------
    smiles : string
        smiles format for compounds.

    Returns
    -------
    mol_3D : rdkit.Chem.rdchem.Mol
        3D mol for compounds.
    '''

    mol_2D = Chem.MolFromSmiles(smiles)
    mol_3D = generate_mol_3D(mol_2D)
    return mol_3D
