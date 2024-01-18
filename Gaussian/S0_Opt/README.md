# 1. Ground State (S0) Geometry Optimization
## References
Opt keyword info: [https://gaussian.com/opt/]

## Files necessary
```.com or .gjf```

#### General Arcitecture of .com file
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
