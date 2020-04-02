## Fight SARS-CoV-2 strategy for postera contribution (started 25.03.2020)
powered by: Yonghui Chen, Dominique Sydow, Jaime Rodríguez-Guerra, Andrea Volkamer (andrea.volkamer@charite.de)

This is part of a community effort to rapidly find new hits to target the virus main protease.

### Background

* https://covid.postera.ai/covid
* https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem/Downloads.html

### Available data and methods
<!-- AV: Clear when done. -->
<!-- JRG: Summarize in # Resources -->

1. Input data: Collected input molecules for screening pipeline
    * Approved drugs
        * [TODO] All
        * Example data set: [Protease inhibitors](https://github.com/volkamerlab/covid19-SBapproach/blob/master/data/proteaseFDAdrugs.csv) (taken from http://dx.doi.org/10.17179/excli2020-1189)
    * SARS-CoV-2 focused ChEMBL subset
        * Binding site comparison based, available [here](https://github.com/volkamerlab/covid19-SBapproach/tree/master/data/focused_library_similar_proteins)
    * Fragments from [DiamondX](https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem/Downloads.html)
        * [Non-covalent hits](https://github.com/volkamerlab/covid19-SBapproach/blob/master/data/fragments/non_covalent_fragments_2D.sdf) in the active site
        * [Covalently-bound hits](https://github.com/volkamerlab/covid19-SBapproach/blob/master/data/fragments/covalent_fragments_2D.sdf) in the active site
    * Current [postera](https://covid.postera.ai/covid) submissions, available [here](https://github.com/volkamerlab/covid19-SBapproach/blob/master/data/covid_submissions_03_24_2020.xlsx)
2. Available methods for pipeline
    * Focused compound library design
        * Protease binding site definition
        * Structure-based binding site comparison using [ProBis](http://probis.cmm.ki.si/)
        * Querying ligands from ChEMBL known to bind to these similar proteins
        * More info available [here](https://github.com/volkamerlab/covid19-SBapproach/tree/master/notebooks/focused_library_similar_proteins)
    * Compound preprocessing and filtering
        * Generate 3D conformations
        * Filter by similarity to fragments
        * [TODO] Select divers subset
        * [TODO] others
    * Docking
       * Dock selected compounds to target ensemble using smina
       * See [Pipeline](https://github.com/volkamerlab/covid19-SBapproach/tree/master/notebooks/Docking).
    * [TODO] Growing
      * SeeSAR for DiamondX fragment growing
    * [TODO] Explore available compounds in REAL space (Availability by Enamine)
        * InfiniSee search using FTrees in REALspace
    * [Skip for now] MD simulations to verify docking results
        * or use [covid moonshot pipeline](https://github.com/FoldingAtHome/covid-moonshot)

### Proposed pipelines (one per submission)
<!-- AV: Clear when done. -->

1. [Trial case to set up pipeline]: Known protease inhibitors
    * Screening data: Protease inhibitors
        * Fragment MCS: only use compounds which contain at least (a decent part of) one fragment
            * Non-covalent fragments used
        * Preprocess molceules
            * Generate 3D
    * Perform docking
        * Ensemble method
        * Select most promising compounds
    * [TODO] Search for most similar compounds in Enamine REAL space
        * Using InfiniSee Software
        * Postprocessing (here or later):
            * Select diverse subset
            * Cross-check with postera submissions
            * Selection of ~20 candidates
    * [TODO] Reevaluate proposed hits
        * Docking
    * [TODO] Submission
2. [TODO] Docking Approach: Start from focused ChEMBL library
    * Screening data: Protease inhibitors
        * Fragment MCS: only use compounds which contain at least (a decent part of) one fragment
            * Non-covalent fragments used
        * Preprocess molceules
            * Generate 3D
    * Perform docking
        * Ensemble method
        * Select most promising compounds
    * Search for most similar compounds in Enamine REAL space
        * Using InfiniSee Software
    * Postprocessing (here or later):
        * Select diverse subset
        * Cross-check with postera submissions
        * Selection of ~20 candidates
    * Reevaluate proposed hits
        * Docking
    * Submission
3. [TODO] Growing approach: Start from DiamondX fragments
    * Screening data: DiamondX fragments
    * Grow fragments
    * Search for most similar compounds in Enamine REAL space
        * Using InfiniSee Software
    * Postprocessing (here or later):
        * as above
    * Reevaluate proposed hits
        * Docking
    * Submission

## Repository structure

<!-- JRG Fill this in -->

## Resources

<!-- AV: List proposed outputs here. -->