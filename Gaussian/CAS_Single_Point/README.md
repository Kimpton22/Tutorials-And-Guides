# 6. Gaussian CASSCF Single Point
Similar to molcas, Gaussian is also able to perform CASSCF calculations (for more details on this method see the molcas/CASSCF tutorial). While the CAS method is implementable in Guassian, it is not recommended over molcas, and should only be used when the results from molcas seem abnormal (usually when molcas generates and odd molecular structure). 
## References
CAS method info: [https://gaussian.com/cas/]

## Files necessary
```.com or .gjf and .sh (not necessary if using python submit script)```

## Keywords and Usage
There are two mandatory keyword for CAS single points in Gaussian which are ```CAS(#ACTIVE_ELECTRONS,#ORBITALS) formcheck```. Note that CAS is it's own method and should replace the DFT method. ```formcheck``` is used to generate a ```.FChk``` file, which allows for viewing of orbitals which is necessary for analysis. **Also note that the largest active space that Gaussian can accomodate without error is an 8,8.**

### Optional Keywords
Within the "CAS" keyword, there are a number of optional modifiers that may aid your calculation. To use these, add them to the opt keyword in this way: ```CAS(#ACTIVE_ELECTRONS,#ORBITALS,OPTION1,OPTION2,OPTION3,...)```. Information for all options can be found here: [https://gaussian.com/cas/]
1. NRoot=j - This requests that states out to the jth excited state be used in the configurational interaction (CI). Combine this with the StateAverage option to include state averaging out to the jth excited state
2. StateAverage - Calculates state averaging out up to the NRoot=j excited state. If this option is used, an additional line at the bottom of the input file (after all xyz coordinates) must be added to provide the weights for each state. It is normal to use equal weighting, so for NRoot=5 with StateAverage, you would add ```0.2 0.2 0.2 0.2 0.2``` to the end of the input file. Also make sure that there are no addition lines (blank or otherwise) after this line.
3. Opt=conical - This is a separate keyword (and would not be put inside of the CAS()) used for optimizing conical intersections with Gaussian. Note that this implicitly applies state averaging as well as approximations to spin-orbit coupling for states.
4. SlaterDet - Required if intersections between singlet and triplet states is desired.

## Analysis
See the molcas/CASSCF section for analysis.

## Restarting CAS jobs with Gaussian
Restarting CAS Gaussian jobs requires a slightly different route line (where all of the job keywords are). ```CASSCF Opt=Restart Extralinks=L405``` is required instead of all other job keywords to restart a CAS job.
