"""
Functions used in binding site definition notebook.
"""

from collections import Counter


from Bio.PDB import PDBParser, Selection, NeighborSearch
import pandas as pd


def get_ligand(chain, ligand_name):
    """
    Get ligand.
    """
    
    for residue in chain.get_residues():
        
        if residue.full_id[3][0] == ligand_name:
            return residue
        

def get_protein(chain):
    """
    Get protein (residues without hetero-residues).
    """
    
    return [residue for residue in chain.get_residues() if residue.full_id[3][0] == ' ']


def get_centroid(residue):
    """
    Get centroid for residue atoms.
    """

    coordinates = pd.DataFrame(
        [atom.get_coord() for atom in residue.get_atoms()],
        columns='x y z'.split()
    )

    return list(coordinates.mean())


def binding_site_residues(structure_path, ligand_name, distance_cutoff):
    """
    Get binding site residues (Biopython objects) from Diamond structure.
    """
    
    # Read structure
    parser = PDBParser()
    structures = parser.get_structure(structure_path.stem, structure_path)

    # Extract protein and ligand
    protein = get_protein(structures[0]['A'])
    ligand = get_ligand(structures[0]['A'], ligand_name)

    # Get residues around ligand centroid
    atoms  = Selection.unfold_entities(protein, 'A')
    ns = NeighborSearch(atoms)
    closest_residues = ns.search(get_centroid(ligand), distance_cutoff, 'R')
    
    return closest_residues


def mulitple_binding_sites_residue_ids(structure_paths, ligand_name, distance_cutoff):
    """
    Get binding site IDs from a set of Diamond structures.
    """

    residue_ids = {}

    for structure_path in structure_paths:

        closest_residues = binding_site_residues(structure_path, ligand_name, distance_cutoff)
        closest_residue_ids = [residue.full_id[3][1] for residue in closest_residues]
        
        residue_ids[structure_path.stem] = closest_residue_ids
        
    return residue_ids


def binding_site_residues_by_coverage(residue_ids, n_structures, coverage_cutoff):
    """
    Get binding site residues from a set of PDB structures, which are greater or equal to a given coverage cutoff.
    """
    
    residue_ids_flat = []
    for residues in residue_ids.values():
        residue_ids_flat = residue_ids_flat + residues

    counter = Counter(residue_ids_flat)
    coverage = pd.DataFrame(counter.items(), columns=['residue_id', 'n_structures'])
    coverage['coverage'] = coverage.n_structures / n_structures
    
    return coverage[coverage.coverage >= coverage_cutoff]


def binding_site_in_pymol(binding_site):
    """
    Get PyMol commands to visualize binding site.
    """
    
    pymol_command = (
        f'fetch 6LU7\n'
        f'remove solvent\n'
        f'select pocket, 6LU7 and resi {"+".join([str(i) for i in binding_site.sort_values("residue_id").residue_id.to_list()])}\n'
        f'show cartoon\n'
        f'hide lines\n'
        f'color blue, pocket\n'
        f'show lines, pocket'
    )
    
    return pymol_command


def binding_site_in_probis(binding_site):
    """
    Get ProBis command to select binding site.
    """
    
    probis_command = (
        f':A and ('
        f'{",".join([str(i) for i in binding_site.sort_values("residue_id").residue_id.to_list()])})'
    )
    
    return probis_command
