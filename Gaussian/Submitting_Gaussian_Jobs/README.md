# 0. Submitting Gaussian Jobs 
Submitting of Gaussian jobs to an HPC cluster requires a ```.sh or .sbatch``` file. You can create this manually for each job you want to run if you are masochistic, however, we have developed a script: ```g16_discovery_lopez.py``` to automatically create and submit these .sh files. This script is specifically designed for the Lopez lab and our HPC called discovery. If you want to use this on another HPC, you will need to change the path directories to Gaussian.

## Usage
Transfer the script to Discovery (or your HPC) and copy the path to where the script is located. Then, go to the directory with you input ```.com/gjf``` file and enter the following line in bash: 

```python /PATH/TO/SCRIPT/g16_discovery_lopez.py FILENAME.com NPROCS TIME(in days) MEMORY```

This automatically creates the necessary ```.sh``` file and submits it to the queue (specifically on the lopez partition). Note that the partition is easily changeable by editing the python script and changing the partition line to whichever partition you want. Alternatively, if you place the script in the diretory with the input file, you can enter this line into bash:

```python g16_discovery_lopez.py FILENAME.com NPROCS TIME(in days) MEMORY```

If you are submitting a lot of gaussian jobs we recommend creating an alias in your .bashrc to call this script easily. 

## Batch submitting jobs
In some cases you may have multiple ```.com/gjf``` files that you want to submit all at the same time. This can be easily done by using a loop in bash:

```for i in *.com; do python g16_discovery_lopez $i NPROCS TIME(in days) MEMORY; sleep 1; done```

This loops through each ```.com``` file in the current directory and submits the job. ```sleep 1``` is required to space out job submissions so that you don't overload the queueing process.
