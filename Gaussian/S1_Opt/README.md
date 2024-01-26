# 7. S1 Optimization
Excited state geometry optimizations in gaussian look to minimize the exctied state energy of a structure by varying geometric parameters in the molecule. It does this using first and sometimes second order derivatives. Geometry optimizations will continue until a) a stationary point is reached on the potential energy surface (PES) b) an error causes the job to end early or c) the maximum number of geometry iterations is reached. This can be completed with TD-DFT methods or with the CASSCF method, though the use of CASSCF for optimization is not recommended and molcas should be used if possible for this method. 
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
Within the "opt" keyword, there are a number of optional modifiers that may aid your calculation. To use these, add them to the opt keyword in this way: opt=(OPTION1,OPTION2,OPTION3,...). Information for all options can be found here: [https://gaussian.com/opt/]

1. calcfc - This option calculates force constants for the molecule which can often speed up optimizations (more direct path to minimum can be found). This can be especially useful for shallow PESs (where large geometric changes result in small energetic changes)
2. recalc=X - This option recalculates the force constants for the molecule every X iterative geometries, which can be especially useful to speed up optimizations.
3. maxstep=X - This option reduces or increases the maximum distance the procedure can move atoms between iterations. This useful for meta-stable intermediates which tend to collapse towards reactants or products. The default is 30 which corresponds to 0.3 bohr or radian units.

## Analysis
See analysis for S0_Opt and TD-DFT

## Restarting CAS jobs with Gaussian
Restarting CAS Gaussian jobs requires a slightly different route line (where all of the job keywords are). ```CASSCF Opt=Restart Extralinks=L405``` is required instead of all other job keywords to restart a CAS job.

