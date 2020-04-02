"""
Check if your candidate compounds have been already submitted to the
Postera.ai spreadsheet. Just provide your candidates in a plain text file
with one SMILES per line and run:

  python check_submitted.py my_compounds.txt

This script does check for SMILES _and_ molecular isomorphism.

It requires Python 3.6+, openforcefield (-c omnia) and tqdm:

  conda install -c conda-forge -c omnia python>=3.6 openforcefield pandas tqdm
"""

import argparse
import logging

logging.disable(logging.CRITICAL)

import pandas as pd
from tqdm import tqdm
from openforcefield.topology import Molecule


BASE_URL = r"https://docs.google.com/spreadsheets/d/{key}/gviz/tq?tqx=out:csv"
# Postera.ai spreadsheet document identifier (found in URL)
SPREADSHEET_ID = "1zELgd-kDEkIjRqc_jdKm5EzDQmRrrYAbErghTPkcA5c"


def parse_cli():
    p = argparse.ArgumentParser()
    p.add_argument(
        "compounds", help="SDF file or a Plain text file with a single SMILES entry per line"
    )

    return p.parse_args()


def smiles_from_txt(path):
    with open(path) as f:
        my_compounds = []
        for line in f:
            line = line.strip()
            if line:
                my_compounds.append(line)
    return my_compounds


def currently_submitted():
    url = BASE_URL.format(key=SPREADSHEET_ID)
    return pd.read_csv(url, usecols=[0]).SMILES.to_list()


def filter_submitted(candidates, submitted):
    """
    Use molecular isomorphism to detect candidate molecules already present in the dataset

    Parameters
    ----------
    candidates : list of str or list of openforcefield.topology.Molecule
        The compounds you want to submit. If list of str, str must be SMILES identifiers
    submitted : list of str
        SMILES for all the compounds already present in the target dataset

    Returns
    -------
    list of str
        SMILES for compounds that are NOT present in the dataset
    """
    from_smiles_options = {"allow_undefined_stereo": True}

    # First, build Molecule objects for our candidate proposals
    if isinstance(candidates[0], str):
        candidates_mols = [
            Molecule.from_smiles(m, **from_smiles_options)
            for m in tqdm(candidates, desc="Building molecules for candidates...")
        ]
    elif isinstance(candidates[0], Molecule):
        candidates_mols = candidates
        candidates = [m.to_smiles() for m in candidates_mols]
    else:
        raise ValueError(
            "Candidates must be a list of SMILES or a list of openforcefield.topology.Molecule objects"
        )

    # Second build Molecule objects for compounds already submitted to the dataset
    submitted_mols = [
        Molecule.from_smiles(m, **from_smiles_options)
        for m in tqdm(submitted, desc="Building molecules for submitted...")
    ]

    valid, already_there = [], []
    for candidate_smiles, candidate_mol in tqdm(
        zip(candidates, candidates_mols), desc="Checking isomorphism...", total=len(candidates)
    ):
        for submitted_smiles, submitted_mol in zip(submitted, submitted_mols):
            if candidate_smiles == submitted_smiles or candidate_mol.is_isomorphic(submitted_mol):
                already_there.append(candidate_smiles)
                break
        else:
            # if we couldn't find a isomorphic compound, we didn't break, so this candidate must be valid
            valid.append(candidate_smiles)
    print(
        "Filtered",
        len(candidates) - len(valid),
        "compounds (already submitted):\n ",
        "\n  ".join(already_there),
    )
    print("Following ones not submitted yet:\n ", "\n  ".join(valid))
    return valid


def main():
    args = parse_cli()
    if args.compounds.endswith(".sdf"):
        print("Building from SDF...")
        my_compounds = Molecule.from_file(args.compounds)
    else:
        my_compounds = smiles_from_txt(args.compounds)
    already_submitted = currently_submitted()
    return filter_submitted(my_compounds, already_submitted)


if __name__ == "__main__":
    main()
