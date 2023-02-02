# Alkane dataset
datasets used for training and evaluating neural networks

Currently consist:

read_h5.py to get statistic of each h5 package.


DFT/

All DFT data are generated with the ωB96x functional and 6-31G(d) basis set.


ANI-1 core/
consists core training data extracted from ANI-1 dataset https://www.nature.com/articles/sdata2017193.
Only hydrocarbons were extracted from the original dataset, 1-4 heavy atoms can be found here, the larger files including 5-8 are too big for github.

MEP/
consists data of the minimum energy path of dissociation for molecules specified in the name of the files. 

NMS/
consists of normal mode sampling data used for training.

g16MD/
consists of MD geometries generated with gaussian16 BOMD algorithm.

aseMD/
consists of MD geometries generated with trained NN ensembles using ASE interface and velocity verlet algorithm.

