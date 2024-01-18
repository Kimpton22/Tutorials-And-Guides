# 2. Single-point CASSCF - Generate CAS orbitals

The RASSCF program in Molcas performs multiconfigurational SCF calculations using the Complete Active Space (CAS) Restricted Active Space (RAS) or the Generalized Active Space (GAS) SCF construction of the wave function. In our case, we will use CASSCF.

## References
RASSCF: https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/rasscf.html


## Files necessary
```.inp```,```.xyz```,```.sh``` and ```.StrOrb``` (ScfOrb from Hartree-Fock)


## Analysis
1. Check that both .log and .status files contain the phrase ```Happy landing!```
2. Open the .rasscf.molden file in ChemCraft to visualize orbitals in the active space (Energy = 0).
3. If the active space is not as planned, submit a new cas-sp using the following steps:
    
    a. Use the orbitals generated from the previous cas-sp (RasOrb) as initial orbitals (StrOrb).
    
    b. Use the alter command to arrange the orbitals in the correct order.
   This keyword is used to change the ordering of MO in INPORB. The keyword requires first the number of pairs to be interchanged, followed, for each pair, the symmetry species of the pair and the indices of the two permuting MOs (Example below)
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

## Analysis
Check .log and .status should have ```Happy landing!```

--- 
---
