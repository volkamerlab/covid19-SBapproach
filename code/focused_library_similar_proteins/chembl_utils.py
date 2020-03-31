"""
Utility functions for ChEMBL queries.
"""

from datetime import datetime
import math

from chembl_webresource_client.new_client import new_client
import pandas as pd


TARGET_API = new_client.target
MOLECULE_API = new_client.molecule
BIOACTIVITY_API = new_client.activity


def targets_by_uniprot_ids(uniprot_ids):
    """
    Get target ChEMBL data by UniProt IDs.
    """
    
    targets_all = []
    
    for uniprot_id in uniprot_ids:
    
        targets = TARGET_API.get(
            target_components__accession=uniprot_id
        ).only(
            'target_chembl_id', 
            'organism', 
            'pref_name', 
            'target_type'
        )
        
        targets = pd.DataFrame.from_dict(targets)
        targets['uniprot_id'] = uniprot_id
        targets_all.append(targets)
        
    targets_all = pd.concat(targets_all, sort=False).reset_index(drop=True)
        
    # Some UniProt IDs return multiple target IDs, keep only first
    targets_all.drop_duplicates(
        'target_chembl_id',
        keep='first',
        inplace=True
    )
        
    return targets_all


def bioactivities_by_target_chembl_ids(target_chembl_ids):
    """
    Get bioactivity ChEMBL data by target ChEMBL IDs.
    """
    
    bioactivities_all = []
    
    for i, target_chembl_id in enumerate(target_chembl_ids):
        
        if i%10 == 0:
            print(f'Progress: {i}/{len(target_chembl_ids)}')
    
        bioactivities = BIOACTIVITY_API.filter(target_chembl_id=target_chembl_id) \
                                     .filter(type='IC50') \
                                     .filter(relation='=') \
                                     .filter(assay_type='B') \
                                     .only(
                                         'activity_id',
                                         'assay_chembl_id', 
                                         'assay_description', 
                                         'assay_type', 
                                         'molecule_chembl_id', 
                                         'type', 
                                         'units', 
                                         'relation', 
                                         'value',
                                         'target_chembl_id', 
                                         'target_organism',
                                         'pref_name'
                                     )
        
        bioactivities = pd.DataFrame.from_dict(bioactivities).reset_index(drop=True)
        
        # Remove entries where any data is missing
        bioactivities.dropna(
            axis=0, 
            how='any', 
            inplace=True
        )
        
        bioactivities_all.append(bioactivities)
        
    bioactivities_all = pd.concat(bioactivities_all, sort=False)
    
    # Some bioactivity entries are return multiple times (I do not know why), keep only first
    bioactivities_all.drop_duplicates(
        'activity_id',
        keep='first',
        inplace=True
    )
    
    return bioactivities_all


def molecules_by_molecule_chembl_ids(molecule_chembl_ids):
    """
    Get molecule ChEMBL data by molecule ChEMBL IDs.
    """
    
    molecules_all = []
    
    for i, molecule_chembl_id in enumerate(molecule_chembl_ids):
        
        if i%1000 == 0:
            print(f'Progress {datetime.now()}: {i}/{len(molecule_chembl_ids)}')
    
        molecules = MOLECULE_API.filter(
            molecule_chembl_id = molecule_chembl_id
        ).only('molecule_chembl_id','molecule_structures')
        
        molecules = pd.DataFrame.from_dict(molecules).reset_index(drop=True)
        molecules_all.append(molecules)
        
    molecules_all = pd.concat(molecules_all, sort=False).reset_index(drop=True)
    
    # Split different molecule structure representations in individual columns
    for key in molecules_all.molecule_structures.iloc[0].keys():
        molecules_all[key] = molecules_all.apply(lambda x: x.molecule_structures[key], axis=1)

    # Drop some columns
    molecules_all.drop(['molecule_structures', 'molfile'], axis=1, inplace=True)   
    
    return molecules_all
    

def standardize_bioactivities(bioactivities):
    """
    Convert IC50 values to nM and calculate pIC50 values.
    """
    
    # Apply unit conversion to each row (=bioactivity entry) of DataFrame
    bioactivity_nM = bioactivities.apply(lambda x: _convert_to_nM(x['units'], x['value']), axis=1)

    # Add converted units and values to DataFrame
    bioactivities['value'] = bioactivity_nM
    bioactivities.rename(columns={'value': 'IC50'}, inplace=True)
    bioactivities['units'] = 'nM'
    
    # Convert IC50 (nM) to pIC50
    bioactivities['pIC50'] = bioactivities.apply(lambda x: _convert_ic50_to_pic50(x.IC50), axis=1)
    
    return bioactivities


def _convert_to_nM(unit, bioactivity):
    """
    Convert IC50 from predefined units to nM.
    """
    
    conversion_factors = {
        "pM": 1e-3,
        "10'-11M": 1e-2,
        "10'-10M": 1e-1,
        "nM": 1e+0,
        "nmol/L": 1e+0,
        "10'-8M": 1e+1,
        "10'-1microM": 1e+2,
        "10'-7M": 1e+2,
        "uM": 1e+3,
        "/uM": 1e+3,
        "10'-6M": 1e+3,
        "10'1 uM": 1e+4,
        "10'2 uM": 1e+5,
        "mM": 1e+6,
        "M": 1e+9,
    }
    
    try:
        return float(bioactivity) * conversion_factors[unit]
        
    except KeyError:
        print(f'Unit not recognized: {unit}')
        return


def _convert_ic50_to_pic50(ic50_value):
    """
    Convert IC50 values in nM to pIC50 values.
    """
    
    pic50_value = 9 - math.log10(ic50_value)
    
    return pic50_value

