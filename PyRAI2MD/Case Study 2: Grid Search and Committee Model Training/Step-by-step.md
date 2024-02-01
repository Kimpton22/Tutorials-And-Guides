# Case Study 2: Grid Search
Quick Explanation heres.

# Step 1: Grid Search
Files needed: 
1. run_PyRAI2MD.sh - submission script for PyRAI2MD
2. input - PyRAI2MD input file specifically for the grid search
3. {filename}.slurm - slurm submission script for the different jobs that will be run during the grid search
4. data-shuffle.json - data collected from the interpolation step

Outputs: 
1. {filename}.log - log file for the PyRAI2MD grid search job.
2. `grid_search` - a folder where all the grid search were done

## Step 1a: Identifying the quickest and most accurate NN committee combination
Files needed: 
1. {filename}.log - log file for the PyRAI2MD grid search job.

The bottom of the log file will look something like the following: 
<img width="1529" alt="Screenshot 2024-02-01 at 3 06 17 PM" src="https://github.com/Kimpton22/Tutorials-And-Guides/assets/66268256/92882fa6-62ab-4a92-9701-044d209cf363">

Note: The bottom half is what we are going to be looking at. The job tracked the hyperparameters that were changed (i.e. `depth`,`layers`,`batch_size`,`reg_l1`, and `reg_l2`) and the time it took them to complete the jobs. We can use an Excel sheet here to organize the data and find the quickest and the lowest MAE value for the energies. 

# Step 3: Create a committee model using the optimal hyperparameters
A committee model is a set of neural networks that will be the starting point for the adaptive sampling step, a step that will optimize the NN committee and expand the data with data points in undersampled regions. 

Files needed: 
1. run_PyRAI2MD.sh - submission script for PyRAI2MD
2. input - PyRAI2MD input file specifically for the committee model training
3. data-shuffle.json - data collected from the interpolation step

Outputs:
1. {filename}.log - will contain the information of the committee model (i.e. MAEs and wall time)
