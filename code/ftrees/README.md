# COVID-19 fast hits: Search within Enamine REAL space to find compounds that are easy to make
This folder contains example script(s) that allow to search for similar compounds in a fragments space using the FTrees functionality.

## Background

To accelerate the whole process, only compounds will be suggested that are available withing Enamine REAL space.
* The search is done using [Ftrees](https://www.biosolveit.de/FTrees/) technology from BioSolveIt:
Explanation from website: 'Feature Trees (short FTrees) is a highly efficient software tool for pharmacophore-style similarity searching, facilitating virtual HTS. The Feature Tree descriptor captures a molecule's overall topology and its pharmacophore properties. The similarity of two such descriptors is based on an alignment (shown above by the color-coding of related functional groups).'
* [REAL space](https://www.biosolveit.de/CoLibri/spaces.html#realspace): The REAL space is used here to allow to find compounds that are easy to make by Enamine.

## Examples ipynb

The notebook shows how to generate similar compounds starting from either a single Smiles or a multi sdf file. As well as how to use the different parameters.

FTrees itself is run from the command line (evoked within the nb), for larger compound sets, it might be more useful to not run it within a nb.