# Case Study 4: Machine Learned - Nonadiabatic Molecular Dynamics
Files that are needed:
1. bd-td.freq.molden – the frequency file used in Wigner sampling
2. data{# of data points}-{number of iteration}.json – the final training data
3. NN-bd-td-## – the final trained NN
4. input – the PyRAI2MD input file
5. Gen-FSSH.py – a python script to generate ML-NAMD simulations
6. sampling – the input to generate ML-NAMD simulations

# Step 1: Initial condition 
This will run a Wigner sampling on the reactant and will create the folders for the initial conditions. This folder should contain the following:
1. {filename}-###.xyz - Wigner sampled geometry
2. run_PyRAI2MD.sh - submission script for the PyRAI2MD job
3. input - PyRAI2MD input file

How to run:
``python3 traj_generator.py control``

Output: 
1. {filename}-[1–###] – subfolders for ML-NAMD simulations
2. runset-[1-##] – submission script for grouped ML-NAMD simulations
3. runall.sh – script to submit all ML-NAMD simulations

To run all the trajectories you will need to submit the runall command.

# Step 2: Analysis
Files that you need are: 
1. traj_analyzer.py - analyzer scripts developed my Jingbai (need to link to Jinbai's github)
2. control files
### 01-diagnosis

This will check for the completeness of the trajectories

Output: 
1. complete - a text file containing a list of all the trajectories that suffice the threshold
### 02-energy_conservation

This will check the energy conservation of the trajectories, we would be able to modify the maximum energy drift value

Output
1. conserved - a text file containing a list of all the trajectories that conserved energy under the maximum energy drift value. There is not a single value that is a standard value for the maximum energy drift and can be optimized for the specific system.

### 03-data_extraction

This will extract the data from the trajectories into a json file

Output: 
1. {filename}.json - json file that contains all the trajectory information. This is used in further steps to speed up the data analysis process, where the script no longer reads the trajectory folders, but the newly created {filename}.json file
   
### 04-state_populations

This will extract the state population data from the json file to create a state population map using the ``plot-2d-state-pop.py`` script
### 05-parameter_tracking

This will extract the specific parameters you want to track for the specific trajectories that conserve energy. 

Outputs: 
1. plot-{filename}.json - json file that contains the different parameters that you measured. This should be in the same order as seen in the `05-parameter_tracking` file
