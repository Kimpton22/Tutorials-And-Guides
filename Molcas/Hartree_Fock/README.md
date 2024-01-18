# Single-point HF - Generate initial orbitals

##  Initial orbitals
The SCF program of the Molcas program system generates closed-shell Hartree–Fock, open-shell UHF, and Kohn–Sham DFT wave functions. It will generate the ```.ScfOrb```, an orbital file that will be used on the CASSCF calculation.

## References
GATEWAY: https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/gateway.html
SEWARD: https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/seward.html    
SCF: https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/scf.html


## Files necessary
```.inp```,```.xyz``` (from dft opt) and ```.sh``` 


## Submission
You should have a directory with all the files mentioned before and use the following command to submit the job:
_Replace XXX.sh by your filename_

```
sbatch XXX.sh
```

## Analysis
Check .log and .status should have ```Happy landing!```

--- 


   
