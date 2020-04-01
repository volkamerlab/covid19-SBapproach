# Focused library

The focused library was constructed based on the following parameters

- `focused_library_divers.csv` (4121 compounds)
  - Similar binding sites to binding site of Sars CoV-2 main protease using ProBis (protease binding site consists of residues that were in 50% of all Diamond XChem screen in an 15 Angström radius around the co-crystallized fragments))
  - Focused library consists of all molecules in ChEMBL that were tested active against these simliar targets; conditions:
    - Target is a single protein
    - Only IC50 values, exact measurements in binding assays
    - Activity defined as pIC50 > 6.3
    
- `focused_library_divers.csv` (109 compounds)
  - Compound clustering using Butina algorithm with 
    - RDKit fingerprint
    - Tanimoto similarity
    - Distance cutoff of 0.6
  - Diverse set consists of cluster centroids