# Case Study 4: Machine Learned - Nonadiabatic Molecular Dynamics
Files that are needed:
1. bd-td.freq.molden – the frequency file used in Wigner sampling
2. data{# of data points}-{number of iteration}.json – the final training data
3. NN-bd-td-## – the final trained NN
4. input – the PyRAI2MD input file
5. Gen-FSSH.py – a python script to generate ML-NAMD simulations
6. sampling – the input to generate ML-NAMD simulations

# Step 1: Initial condition 
How to run:
``python3 traj_generator.py control``

Output: 
1. {filename}-1–###] – subfolders for ML-NAMD simulations
2. runset-[0–20] – submission script for grouped ML-NAMD simulations
3. runall.sh – script to submit all ML-NAMD simulations
