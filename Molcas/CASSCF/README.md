# 2. Single-point CASSCF - Generate CAS orbitals

The RASSCF program in Molcas performs multiconfigurational SCF calculations using the Complete Active Space (CAS) Restricted Active Space (RAS) or the Generalized Active Space (GAS) SCF construction of the wave function. In our case, we will use CASSCF.

## References
RASSCF: https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/rasscf.html


## Files necessary
```.inp```,```.xyz```,```.sh``` and ```.StrOrb``` (ScfOrb from Hartree-Fock)


## Analysis
1. Check .log and .status should have ```Happy landing!```
2. Open .rasscf.molden on ChemCraft to vizualize orbitals in the active space (Energy = 0)
3. If active space is not as planned, a new cas-sp will be submitted:
   
   a. Use the orbitals generated from previous cas-sp (RasOrb) as initial orbitals (StrOrb)
   
   b. Use the alter command to get orbitals in the correct order
   
   c. Repeat the steps a and b as needed


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
