# How to Restart a Job
Sometimes a job will fail and you will want to restart it exactly where it left off. Restarting is not recommended for all failure types and is most useful for timeouts, node failures, or other HPC end failures. If you want to restart a job, you will need the saved checkpoint ```.chk``` file along with a ```.com or .gjf``` file. Saving and providing the ```.rwf``` file can also useful and can marginally speed up restarted jobs.

Set up the input file like any other input file, expect for the lines that start with ```%chk and #```. After ```%chk``` write ```=/PATH/TO/CHK/CHK_FILE.CHK```. On the ```#``` line, replace everything with the keyword ```Restart```. 

It is critical to ensure that this file is set up correctly, because submitting a restart with an error in the input will overwrite the checkpoint file, making it impossible to restart the job from where it left off. 


## Example Restart Input
```
%mem=80Gb
%nprocshared=16
%chk=/scratch/larmore.s/example.chk
%rwf=/scratch/larmore.s/example.rwf (optional if you have the .rwf)

# Restart

TITLE

CHARGE SPIN_MULTIPLICITY
XYZ COORDINATES
```
