# Optimization  

## References
SLAPAF: https://www.molcas.org/documentation/manual/node115.html

Provided with the first order derivative with respect to nuclear displacements the program is capable to optimize molecular structures with or without constraints for minima or transition states. 

## Files necessary
```.inp```,```.xyz```,```.sh``` and ```.StrOrb``` (RasOrb from CASSCF)

## Submission
You should have a directory with all the files mentioned before and use the following command to submit the job:
_Replace XXX.sh by your filename_

```
sbatch XXX.sh
```


## Analysis
1. Check that both .log and .status files contain the phrase ```Happy landing!```
2. Open the ```.Opt.xyz``` file in ChemCraft to visualize your geometry also .



 
---


