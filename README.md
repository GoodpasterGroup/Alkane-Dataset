# Alkane dataset
datasets used for training and evaluating neural networks in the following work:
Neural Network Potentials for Reactive Chemistry: CASPT2 Quality Potential Energy Surfaces for Bond Breaking
https://doi.org/10.26434/chemrxiv-2023-13cv6


Currently consist:

read_h5.py to get statistic of each h5 package.


DFT/

All DFT data are generated with the ωB96x functional and 6-31G(d) basis set. Sample Gaussian16 input script included.

DFT/ANI-1 core/
consists core training data extracted from ANI-1 dataset https://www.nature.com/articles/sdata2017193.
Only hydrocarbons were extracted from the original dataset, 1-4 heavy atoms can be found here, the larger files including 5-8 are too big for github.

DFT/MEP/
consists data of the minimum energy path of dissociation for molecules specified in the name of the files. 

DFT/NMS/
consists of normal mode sampling data used for training.

DFT/g16MD/
consists of MD geometries generated with gaussian16 BOMD algorithm.

DFT/aseMD/
consists of MD geometries generated with trained NN ensembles using ASE interface and velocity verlet algorithm.

CASPT2/

All CASPT2 are generated following algorithm in the paper above. Sample molpro input script included.

CASPT2/MEP/
consists data of the minimum energy path of dissociation for molecules specified in the name of the files. 

CASPT2/NMS/
consists of normal mode sampling data used for training.

CASPT2/aseMD/
consists of MD geometries generated with trained NN ensembles using ASE interface and velocity verlet algorithm.
