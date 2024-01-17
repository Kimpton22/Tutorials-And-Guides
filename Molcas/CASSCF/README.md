# 2. Single-point CASSCF - Generate CAS orbitals

## References
RASSCF: [https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/gateway.html](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/rassi.html)

## Files necessary
```.inp```,```.xyz```,```.sh``` and ```.StrOrb``` (ScfOrb  from previous step)

#### .inp example
```
&GATEWAY
 coord=$Project.xyz
 basis=ano-s-vdzp
 group=C1
 RICD

&SEWARD
 doanalytic

&RASSCF
 FileOrb=$Project.StrOrb
 Spin=1
 Charge=0
 NActel=8
 Ras2=9
 CIRoot=8 8 1
```

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
 coord=$Project.xyz
 basis=ano-s-vdzp
 group=C1
 RICD

&SEWARD
 doanalytic

&RASSCF
 FileOrb=$Project.StrOrb
 Spin=1
 alter
 1
 1 58 33
 Charge=0
 NActel=8
 Ras2=9
 CIRoot=8 8 1
```


---
