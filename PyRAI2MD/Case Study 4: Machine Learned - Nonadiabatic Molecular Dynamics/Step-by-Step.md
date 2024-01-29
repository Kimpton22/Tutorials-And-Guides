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
3. {}

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
- 01-diagnosis
- 02-energy_conservation
- 03-data_extraction
- 04-state_populations
- 05-parameter_tracking
