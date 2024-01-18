#Case Study 3: Active learning - Adaptive sampling
This step will allow you to extend your initial training set to undersample regions through the usage of a committee of NN. 

Files that you need: 
1. input – PyRAI2MD input file specifically for adaptive sampling. 
2. run_PyRAI2MD.sh – submission script
3. {filename}-shuffled.json– initial training data from the interpolation step and the one used for the committee model training and grid search steps
4. NN-bd-td – the committee model that was created using the optimal hyperparameters
5. Sampling conditions either of the following:
  a. {filename}.init.xyz – initial conditions often generate with the Wigner sampling
  b. {filename}.freq.molden – frequency data (format molden)
6. 	{filename}.molcas – Molcas input
7. 	{filename}.StrOrb – Molcas guess orbital file
8. 	{filename}.slurm – SLURM template


Outputs: 
1. {filename}-[1–###] – ML-NAMD subfolders that are running to collect the data points
2. {filename}.log – PyRAI2MD log file
3. {filename}-ntraj-5-iter-n.xyz – coordinates of the collected geometries
4. {filename}.adaptive.json – adaptive sampling geometry data
5. NN-{filename}-n – Updated NN model
6. NN-{filename}-n.log – NN training log file that contains the updated MAEs

What to look for: 
You will need to look at the log files of each of the iterations (i.e., `NN-bd-td-n.log`) to determine whether the MAE is still within chemical accuracy (0.043 eVs or 1 kcal/mol)

Naturally, some iterations will have high MAEs as they explore undersampled regions of the potential energy surfaces (PESs), but they will eventually lower. Normally the last iteration will have a good MAE (i.e., < 0.043 eVs) and will have expanded the data set substantially. More rigid molecules have been observed to have their data sets expanded less when compared to more flexible counterparts. If the MAEs within the iterations are not observed to be lowering, check the structures of the collected data to determine whether these structures are possible. 

