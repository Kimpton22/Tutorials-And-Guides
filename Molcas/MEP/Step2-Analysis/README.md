Using the files in the previous step you will preform an analysis on each of the steps of the MEP

Create a directory within the MEP job directory called analysis
In such directory create a input file, the .mep.molden file, the job .strorb file

Using find-mep.py run the command line 
"python3 find-mep.py jobname.mep.molden"

A series of xyz of each of xyz files will be created, each one being a step of the MEP. 
Next run the 1D-cas.py script like so:
