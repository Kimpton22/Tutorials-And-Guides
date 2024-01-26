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
There are two mandatory keywords for TD-DFT optimizations in Gaussian which are ```td=(root=1) opt```.  ```td``` requests a TD-DFT job and ```(root=1)``` specifies the first excited state. ```Opt``` requests a minimum optimization on the PES.

### CASSCF
There are two mandatory keywords for CAS optimizations in Gaussian which are ```CAS(#ACTIVE_ELECTRONS,#ORBITALS,NRoot=j) opt```. ```CAS``` indicates the method and NRoot=j specifies the desired state to optimized on, where 1 is the ground state (different from TD-DFT where 1 is the first excited state). ```Opt``` requests a minimum optimiztion on the PES. **Note that the largest active space that Gaussian can accomodate without error is an 8,8.**

### Optional Keywords
#### TD-DFT

#### CAS
Within the "CAS" keyword, there are a number of optional modifiers that may aid your calculation. To use these, add them to the opt keyword in this way: ```CAS(#ACTIVE_ELECTRONS,#ORBITALS,OPTION1,OPTION2,OPTION3,...)```. Information for all options can be found here: [https://gaussian.com/cas/]
1. NRoot=j - This requests that states out to the jth excited state be used in the configurational interaction (CI). Combine this with the StateAverage option to include state averaging out to the jth excited state
2. StateAverage - Calculates state averaging out up to the NRoot=j excited state. If this option is used, an additional line at the bottom of the input file (after all xyz coordinates) must be added to provide the weights for each state. It is normal to use equal weighting, so for NRoot=5 with StateAverage, you would add ```0.2 0.2 0.2 0.2 0.2``` to the end of the input file. Also make sure that there are no addition lines (blank or otherwise) after this line.
3. Opt=conical - This is a separate keyword (and would not be put inside of the CAS()) used for optimizing conical intersections with Gaussian. Note that this implicitly applies state averaging as well as approximations to spin-orbit coupling for states.
4. SlaterDet - Required if intersections between singlet and triplet states is desired.

## Analysis
See the molcas/CASSCF section for analysis.

## Restarting CAS jobs with Gaussian
Restarting CAS Gaussian jobs requires a slightly different route line (where all of the job keywords are). ```CASSCF Opt=Restart Extralinks=L405``` is required instead of all other job keywords to restart a CAS job.

