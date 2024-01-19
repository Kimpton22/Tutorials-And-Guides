# 0. Submitting Gaussian Jobs 
Submitting of Gaussian jobs to an HPC cluster requires a ```.sh or .sbatch``` file. You can create this manually for each job you want to run if you are masochistic, however, we have developed a script: ```g16_discovery_lopez.py``` to automatically create and submit these .sh files. This script is specifically designed for the Lopez lab and our HPC called discovery. If you want to use this on another HPC, you will need to change the path directories to Gaussian. 

## Usage
Make to transfer the script to Discovery (or your HPC) and copy the path to where the script is located. Then, go to the directory with you input ```.com/gjf``` file and enter the following line in bash: 

```python /PATH/TO/SCRIPT/g16_discovery_lopez.py FILENAME.com NPROCS TIME(in days) MEMORY```

Alternatively, if you place the script in the diretory with the input file, you can enter this line into bash:

```python g16_discovery_lopez.py FILENAME.com NPROCS TIME(in days) MEMORY```
