## Fight SARS-CoV-2 strategy for postera contribution (started 25.03.2020)
powered by: Yonghui Chen, Dominique Sydow, Jaime Rodríguez-Guerra, Andrea Volkamer (andrea.volkamer@charite.de)

This is part of a community effort to rapidly find new hits to target the virus main protease.

### Background
The COVID-19 (coronavirus disease 2019) pandemic, caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) has become a global health emergency. With no current evidence for specific antiviral treatment, there is an urgent need for effective anti-COVID drugs ([more about potential drugs and clinical trials in the COVID-10 Science Report: Therapeutics](https://sph.nus.edu.sg/wp-content/uploads/2020/03/COVID-19-Science-Report-Therapeutics-30-Mar.pdf)). A promising target is the main protease M<sup>pro</sup> of SARS-CoV-2 for which the first [crystal structure](http://www.rcsb.org/structure/6LU7) has been determined in January 2020.  
[UK’s Diamond Light Source](https://www.diamond.ac.uk/covid-19/for-scientists/Main-protease-structure-and-XChem/Downloads.html) performed a large crystal based fragment screen on M<sup>pro</sup>. In collaboration with [PostEra](https://covid.postera.ai/covid) and others, they encourage researchers from around the world to use their fragment hits as a starting point and contribute, amongst others, by suggesting potential inhibitors. 

References:

* Jin, Zhenming, <i>et al.</i> "Structure-based drug design, virtual screening and high-throughput screening rapidly identify antiviral leads targeting COVID-19." bioRxiv (2020).
* Zhang, Linlin, <i>et al.</i> "Crystal structure of SARS-CoV-2 main protease provides a basis for design of improved α-ketoamide inhibitors." Science (2020).
* Lai, Chih-Cheng, <i>et al.</i> "Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) and corona virus disease-2019 (COVID-19): the epidemic and the challenges." International journal of antimicrobial agents (2020): 105924.
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