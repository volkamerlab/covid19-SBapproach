## Fight SARS-CoV-2 strategy for postera contribution (started 25.03.2020)
powered by: Yonghui Chen, Dominique Sydow, Andrea Volkamer (andrea.volkamer@charite.de)

This is part of a community effort to rapidly find new hits to target the virus main protease.

### Background

* https://covid.postera.ai/covid
* https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem/Downloads.html

### Pipeline

1. Collect input molecules for screening pipeline
    * Approved drugs 
        * (All)
        * Protease inhibitors (taken from http://dx.doi.org/10.17179/excli2020-1189)
    * SARS-CoV-2 focused ChEMBL subset (probably protease centered)
        * (import and describe work by Dominique https://github.com/dominiquesydow/covid19)
    * [TODO] Fragments from DiamondX
        * Non-covalent hits in the active site
        * Covalently-bound hits in the active site
    * Current [postera](https://covid.postera.ai/covid) submissions
2. Two Approaches for complex generation: Docking and Growing
    * Docking
       * [TODO] Maybe use fragments to filter down compounds
       * Dock selected compounds to target ensemble using smina
       * See [Pipeline](https://github.com/volkamerlab/covid19-SBapproach/tree/master/notebooks/Docking).
    * [TODO] Growing
      * SeeSAR for DiamondX fragment growing
3. [TODO] Collect best compounds from both apporaches
    * Select diverse subset
    * Cross-check with postera submissions
    * Selection of ~20 candidates
4. [TODO] Explore available compounds in REAL space (Availability by Enamine)
    * InfiniSee search in REALspace   
5. [TODO] Reevaluate promising compounds
    * Docking and clustering
    * MD simulations or use [covid moonshot pipeline] (https://github.com/FoldingAtHome/covid-moonshot)
  
    
