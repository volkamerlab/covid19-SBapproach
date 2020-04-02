## Docking screening for focused library filtered from similar proteins
In this pipeline, a docking-based screening will be implemented with the SARS-CoV-2 focused ChEMBL libarary, which filtered from similar protiens, to search the hit compounds.

First, the focused library will be generated (See [here](https://github.com/volkamerlab/covid19-SBapproach/tree/master/code/focused_library_similar_proteins)).
Next, the focused library will be filtered by the maximum common substructure (MCS) fragment strategy. Only those molecules having some resemblance with the original fragments will be choosed (See [here](https://github.com/volkamerlab/covid19-SBapproach/tree/master/notebooks/filter_screeningdeck_by_fragment_similarity.ipynb)).
Finally, the docking-based screening will be applied to the filtered library (See [here](https://github.com/volkamerlab/covid19-SBapproach/tree/master/code/docking)).

### Pipeline
1. Generate the SARS-CoV-2 focused ChEMBL library. It contains 4121 compounds and locates [here](https://github.com/volkamerlab/covid19-SBapproach/tree/master/data/focused_library_similar_proteins/focused_library.csv).
2. Filter the focused library with the MCS fragment strategy.
    * Choose the focused library as screening deck.
    * Choose the 22 [non-covalent fragments](https://github.com/volkamerlab/covid19-SBapproach/tree/master/data/fragments/non_covalent_fragments2D.sdf) as fragment set.
    ![alt text](img/non_covalent_fragments.png "non-covalent fragments")
    * Get MCS between compounds and fragments and store the best-match fragment for per compound.
    
      Part of compounds with the best-match fragment highlighting:
    ![alt text](img/highlight_best_fragments.png "part of the compounds with highlight-best-fragment")
    * Store dataset filtered by similarity to fragment or MCS with fragment.
      * Set the cut-off = 0.75 for the similarity filtering.

        In this case, 916 compounds are filtered.
        ```
        mcsFragName   number
        Mpro-x0995    760
        Mpro-x0305     83
        Mpro-x0107     45
        Mpro-x0387     37
        Mpro-x0946     35
        Mpro-x0967      1
        ```
        The dataset was saved as [focused_library_mcs075.csv](https://github.com/volkamerlab/covid19-SBapproach/tree/master/focused_library_docking_screening_pipeline/result_data/focused_library_mcs075.csv)
      * Control the number of compounds and receptor structures.
        * Compounds

            For the mcs fragments which match more than 50 compounds, they usually are small fragment.

            We control the number of compounds for each mcs fragments no more than 50. The dataset was saved as [focused_library_mcs075_controled.csv](https://github.com/volkamerlab/covid19-SBapproach/tree/master/focused_library_docking_screening_pipeline/result_data/focused_library_mcs075_controled.csv)

        * Receptor structures

            Because of resource-saving, only three strutures were choosed for molecular docking.

            The corresponding fragment ligands for the choosed structures should be big enough and bind with receptor in different subpockets.

            For this pipeline, we choosed sturctures "Mpro-x0387", "Mpro-x0946" and "Mpro-x0967".
            ![alt text](img/receptor_structures.png "receptor_structures")
3. Molecular docking  screening.
   * Docking program: Smina
   * Results analyse:
     * The top 5 compounds in docking screening:
            ![alt text](img/docking_results_top5.png "docking_results_top5")

        Problem:

        We can see that some of the top compounds are similar. In this  situation, it's necessary to cluster and reduce the similar compounds in the screening deck before docking.

     *  The pose of the top 1 comppound, "CHEMBL2059095", in structure "Mpro-x0946":
            ![alt text](img/docking_pose_top1.png "docking_pose_top1")
            It's indicated there is a hydrogen bond between the carbonly of GLN189 and the NH of uramino in small molecule.  
     * Finally picking
            
            Because of the similarity of the compounds, we go through the top 30 compounds and cluster the structures of the compounds manually. For per cluster, the best-scoring compound will be kept.
            
            Finally, we got 7 compounds which recommened to be hit compounds:
            ![alt text](img/recommend_top7.png "recommend_top7")
            
            The poses of the recommened top 7 compounds in structure "Mpro-x0946":
            ![alt text](img/recommend_top7_poses.png "recommend_top7_poses")
            
            It's shown that the 7 recommended compounds locate in the binding site. 
      

