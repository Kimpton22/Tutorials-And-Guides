# 1. Ground State (S0) Geometry Optimization
Ground state geometry optimizations in gaussian look to minimize the energy of a structure by varying geometric parameters in the molecule. It does this using first and sometimes second order derivatives. Geometry optimizations will continue until a) a stationary point is reached on the potential energy surface (PES) (stationary points includes TSs and minima) b) an error causes the job to end early or c) the maximum number of geometry iterations is reached.
## References
Opt keyword info: [https://gaussian.com/opt/]

## Files necessary
```.com or .gjf and .sh (not necessary if using python submit script)```

#### Example .com file
```
%nprocshared=8
%mem=20GB
%chk=tropone.chk
# pbe0/aug-cc-pvdz opt

tropone-pbe0-auccpvdz

0 1
 C                  1.84403100    0.67956600    0.00008700
 C                  1.84403100   -0.67956600    0.00008600
 C                  0.71593700   -1.56011300   -0.00005200
 C                  0.71593700    1.56011300   -0.00005200
 C                 -0.61242500   -1.28111400   -0.00014100
 C                 -0.61242400    1.28111500   -0.00014200
 H                  2.81720700    1.16768300    0.00016800
 H                  2.81720700   -1.16768400    0.00016600
 H                  0.96990100   -2.62001000   -0.00005000
 H                  0.96990100    2.62001000   -0.00004900
 H                 -1.30305400   -2.12354400   -0.00023300
 H                 -1.30305500    2.12354300   -0.00023500
 O                 -2.55083000    0.00000000    0.00019900
 C                 -1.32199800    0.00000000   -0.00001300
```

#### Common Error Messages and Solutions

1. 
