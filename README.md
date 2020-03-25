## Fight SARS-CoV-2 strategy for postera contribution 
Andrea Volkamer (andrea.volkamer@charite.de, 25.03.2020)

This is part of a community effort to rapidly find new hits to target the virus main protease.

### Background

* https://covid.postera.ai/covid
* https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem/Downloads.html

### Pipeline

1. Input molecules
    * Approved drugs 
        * (All)
        * Protease inhibitors (taken from http://dx.doi.org/10.17179/excli2020-1189)
    * SARS-CoV-2 focused ChEMBL subset (probably protease centered)
        * (import and describe work by Dominique https://github.com/dominiquesydow/covid19)
    * Fragments from DiamondX
        * Non-covalent hits in the active site
        * Covalently-bound hits in the active site
    * Current postera (https://covid.postera.ai/covid) submissions
2. Two Approaches: Docking and Growing
    * Docking
       * (Maybe use fragments to filter down compounds)
       * Docked compounds to target, tool (tbd e.g. smina and others)
    * Growing
      * SeeSAR for DiamondX fragment growing
3. Collect best compounds from both apporaches
    * Select diverse subset
    * Cross-check with postera submissions
    * Selection of 20 candidates
4. Explore available compounds in REAL space (Availability by Enamine)
    * InfiniSee search in REALspace   
5. Reevaluate promising compounds
    * Docking and clustering
    * MD simulations
  
    
