"""
Utility functions for ProBis data.
"""

import itertools
from pathlib import Path

import pandas as pd

def parse_ligand_tables(ligand_table_path, concat=True):
    """
    Parse ProBis ligand table, i.e. predlig_XXXXA.csv download file.
    Contains predictions for different data types (small molecules, proteins, nucleic, and ion) and different binding sites.
    
    Parameters
    ----------
    ligand_table_path : pathlib.Path or str
        Path to ProBis ligand table.
    concat : bool
        Concatenate all tables in this file (default is True).
        
    Returns
    -------
    pandas.DataFrame or dict of dict of DataFrame
        ProBis ligand table: One table for all data or individual tables for each data type and binding site.
    """
    
    ligand_table_path = Path(ligand_table_path)
    
    # Read csv lines
    with open(ligand_table_path) as f:
        ligand_lines = f.readlines()

    # Save header
    header = ligand_lines[0][:-1].split('\t')

    # Split lines by empty rows
    # Each list's first elements is data type (i.e. small molecules, protein, nucleic, or ion)
    ligand_lines_split = [list(group) for k, group in itertools.groupby(ligand_lines[1:], lambda x: x == '\n') if not k]

    # Use data types as dictionary keys
    data = {
        data_type[0][:-1]: data_type[1:] for data_type in ligand_lines_split
    }

    # Now do the same for each binding site within each data type
    for data_type_name, data_type in data.items():

        # Get tables 
        data_type_split = itertools.groupby(data_type, lambda x: x[:12] == 'Binding Site')
        tables = [list(group) for k, group in data_type_split if not k]

        # Get keys
        data_type_split = itertools.groupby(data_type, lambda x: x[:12] == 'Binding Site')
        keys = [list(group) for k, group in data_type_split if k]

        # Format each table and save it in dict by binding site name as key
        table_dict = {}
        for key, table in zip(keys, tables):

            table = [row[:-1].split('\t')[1:] for row in table]
            table = pd.DataFrame(table, columns=header[1:])
            table = table.astype(
                {column_name: dtype for column_name, dtype in zip(header[1:], 'str str str float str'.split())}
            )

            table_dict[key[0][:-1]] = table

        # Add table to main data object by data type and binding site
        data[data_type_name] = table_dict
        
    if concat:
        data_tmp = []

        for data_type_name, data_type in data.items():
            for binding_site_name, binding_site in data_type.items():

                binding_site = binding_site.copy()

                binding_site.insert(0, 'Data type', data_type_name)
                binding_site.insert(1, 'Binding site name', binding_site_name)
                data_tmp.append(binding_site)

        data = pd.concat(data_tmp)
    
    return data 