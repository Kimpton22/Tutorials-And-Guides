# 7. S1 Optimization
Excited state geometry optimizations in gaussian look to minimize the exctied state energy of a structure by varying geometric parameters in the molecule. It does this using first and sometimes second order derivatives. Geometry optimizations will continue until a) a stationary point is reached on the potential energy surface (PES) b) an error causes the job to end early or c) the maximum number of geometry iterations is reached. This can be completed with TD-DFT methods or with the CASSCF method. 
## References
DFT method info: [https://gaussian.com/dft/]
Time-Dependent info: [https://gaussian.com/td/]
CAS method info: [https://gaussian.com/cas/]

## Files necessary
```.com or .gjf and .sh (not necessary if using python submit script)```

## Keywords and Usage
### TD-DFT
There are two mandatory keywords for TD-DFT optimizations in Gaussian which are ```td=(root=1) opt freq=noraman```.  ```td``` requests a TD-DFT job and ```(root=1)``` specifies the first excited state. ```Opt``` requests a minimum optimization on the PES. ```freq=noraman``` requests a frequency calculation so that the structure can be confirmed as a minimum on the PES. 

### CASSCF
There are two mandatory keywords for CAS optimizations in Gaussian which are ```CAS(#ACTIVE_ELECTRONS,#ORBITALS,NRoot=j) opt freq=noraman```. ```CAS``` indicates the method and NRoot=j specifies the desired state to optimized on, where 1 is the ground state (different from TD-DFT where 1 is the first excited state). ```Opt``` requests a minimum optimiztion on the PES. ```freq=noraman``` requests a frequency calculation so that the structure can be confirmed as a minimum on the PES. **Note that the largest active space that Gaussian can accomodate without error is an 8,8.**

### Optional Keywords


## Analysis
See the molcas/CASSCF section for analysis.

## Restarting CAS jobs with Gaussian
Restarting CAS Gaussian jobs requires a slightly different route line (where all of the job keywords are). ```CASSCF Opt=Restart Extralinks=L405``` is required instead of all other job keywords to restart a CAS job.

