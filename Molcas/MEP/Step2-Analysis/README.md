### How to run a MEP analysis
## Step1 
Using the files in the previous step you will preform an analysis on each of the steps of the MEP

Create a directory within the MEP job directory called analysis
In such directory create a new input file, and copy the .mep.molden file, the job .strorb file from the MEP direcotry

Using find-mep.py run the command line:
*python3 find-mep.py jobname.mep.molden*

A series of xyz of each of xyz files will be created, each one being a step of the MEP. 
Put all of the generated xyz files into a directory and name it coord

## Step2 
in the 1D-cas.py script change the number of idim to the number of MEP steps you have generated
Next run the 1D-cas.py script like so:
*python3 1D-cas.py jobname.inp*

This will create a series of directories for each MEP step
Each directory is one job, sbatch the Srun_molcas.sh to start the string of jobs
The input used is a XMS-CASPT2 input file
