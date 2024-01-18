# 1. Ground State (S0) Geometry Optimization
Ground state geometry optimizations in gaussian look to minimize the energy of a structure by varying geometric parameters in the molecule. It does this using first and sometimes second order derivatives. Geometry optimizations will continue until a) a stationary point is reached on the potential energy surface (PES) (stationary points includes TSs and minima) b) an error causes the job to end early or c) the maximum number of geometry iterations is reached.
## References
Opt keyword info: [https://gaussian.com/opt/]

## Files necessary
```.com or .gjf and .sh (not necessary if using python submit script)```

## Keywords
The only mandatory keyword for geometry optimizations is ```opt```. 

## Output
The output from the geometry optimization is contained in the ```.log``` file. You should check the end of this file to see if the job succeeded or failed. A successful 
