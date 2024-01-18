# General Input File Structure
```
%mem=XGB (give some memory)
%nprocshared=X (give some number of processors)
%chk=FILENAME.chk (saves a checkpoint file so that the job can be restarted if the job fails)

# FUNCTIONAL/BASIS_SET JOB_KEYWORDS

JOB_TITLE (This is required)

CHARGE SPIN_MULTIPLICITY
XYZ COORDS

CONSTRAINT SETTINGS (required only for scans and constrained optimizations)
```

## Some general notes
### MEMORY
The amount of memory you should give depends on a) the requirements of the job and b) the limit of RAM availble to nodes on your HPC. a) For large jobs (like ab-initio MP2 or sometimes IRCs), lots of memory is required (100+ GB). b) The RAM limit depends on the exact HPC. It's good to double check this with your computing staff, but at Northeastern the maximum RAM memory is 256 GB.

### NPROCS
The number of processors you should request also depends on the size of the job. A good starting point is 8 processors, but if the jobs run very slowly, you may want to increase the number of processors. It's a good idea to request processors in powers of 2 (i.e. 1, 2, 4, 8, or 16). Unfortunately for jobs run with gaussian, more than 16 processors does not substantially decrease run time, so it is not recommended to request more than 16 processors.

### FUNCTIONALS
The correct choice of functional will depends heavily on the molecule of interest and the compromise between cost and accuracy that you want. Gaussian has a number of DFT functionals which you can read about here: ```https://gaussian.com/dft/```. It also offers some ab-initio methods like the MPn and coupled cluster (CC) functionals which you can read about here: ```https://gaussian.com/mp/``` and here: ```https://gaussian.com/cc/```. Note that these MPn and coupled cluster (CC) methods are extremely costly and is recommended only for small systems (i.e. <30-40 heavy atoms [i.e. carbon]).

### BASIS SETS
Similar to functionals, basis set choice also depends on the molecule of interest and the cost/accuracy you want for the job. For a list of basis sets that gaussian offers see: ```https://gaussian.com/basissets/```. A good starting point for most calculations is a simple pople basis set (i.e. 6-31G or 6-31G(d,p)). Each basis set usually has multiple options to add corrections for things like polarization and diffusion. Note that basis sets cannot describe all atoms on the periodic table. Most methods can describe elements Hydrogen --> Krypton, but each basis set has its own limits. For this information check the bottom of the g16 manual for basis sets (linked above in this section).

### JOB KEYWORDS
This depends on what you want to do with Gaussian and the various options are expanded upon in the sub-folders of this Gaussian directory. 
