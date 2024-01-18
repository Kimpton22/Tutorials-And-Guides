# Optimization  

## References
SLAPAF: https://www.molcas.org/documentation/manual/node115.html
Provided with the first order derivative with respect to nuclear displacements the program is capable to optimize molecular structures with or without constraints for minima or transition states. 

## Files necessary
```.inp```,```.xyz```,```.sh``` and ```.StrOrb``` (RasOrb from CASSCF)


## Analysis
1. Check that both .log and .status files contain the phrase ```Happy landing!```
2. Open the ```.rasscf.molden``` file in ChemCraft to visualize orbitals in the active space (Energy = 0).
3. If the active space is not as planned, submit a new CASSCF using the following steps:
    
    a. Use the orbitals generated from the previous cas-sp (```RasOrb```) as initial orbitals (```StrOrb```).
    
    b. Use the ```alter``` command to change the orbital order.
   _This keyword is used to change the ordering of MO in INPORB. The keyword requires first the number of pairs to be interchanged, followed, for each pair, the symmetry species of the pair and the indices of the two permuting MOs (Example below)_
   
    c. Repeat steps a and b as necessary.

#### .inp example with alter
```
&GATEWAY
 coord=$MOLCAS_PROJECT.xyz
 basis
 ano-rcc-vdzp
 Group=c1
 RICD

&SEWARD
doanalytic

&RASSCF
 fileorb=$MOLCAS_PROJECT.StrOrb
 alter
 3
 1 60 57
 1 65 67
 1 66 73
 Spin=1
 Charge=0
 Nactel=10 0 0
 Ras1=0
 Ras2=8
 Ras3=0
 ITERATIONS=200,100
 CIRoot=6 6 1
 Rlxroot=1
```

## Submission
You should have a directory with all the files mentioned before and use the following command to submit the job:
_Replace XXX.sh by your filename_

```
sbatch XXX.sh
```
 
---


