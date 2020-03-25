## Fight SARS-CoV-2 strategy for postera contribution 
Andrea Volkamer (andrea.volkamer@charite.de, 25.03.2020)

This is part of a community effort to rapidly find new hits to target the virus main protease.

### Background

* https://covid.postera.ai/covid
* https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem/Downloads.html

### Pipeline

1. Input molecules
  A. Approved drugs 
  B. SARS-CoV-2 focused ChEMBL subset (probably protease centered)
  C. Fragments from DiamondX
      * Non-covalent hits in the active site
  D. Current postera submissions
      * Covalently-bound hits in the active site
2. Docking and Growing
  A. Docking
      * (Maybe use fragments to filter down compounds)
      * Docked compounds to target, tool tbd
  B. Growing
      * SeeSAR for DiamondX fragment growing
3. Collect best compounds from both apporaches
  A. Select diverse subset
  B. Cross-check with postera submissions
  C. Selection of 20 candidates
4. Explore available compounds in REAL space (Availability by Enamine)
  A. InfiniSee search in REALspace   
5. Reevaluate promising compounds
  A. Docking and clustering
  B. MD simulations
  
    