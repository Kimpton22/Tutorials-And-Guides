# Step 1: Interpolation
Files that are needed: 
1. interpolation.sh - shell script that will run the geodesic interpoation
2. point1-point2.xyz - an xyz file that contains 2 geometries; (1) reactant geometry (i.e. point 1) and (2) the product geometry (i.e. point 2). These are the two points where the geodesic interpolation will be done for.

How to run:
``` 
bash interpolation.sh {xyz file containing both geometries} {number of steps}
```

Example:

```
bash interpolation.sh reactant_meci.xyz 20
```

Outputs: 
1. output.xyz - a xyz file that contains all the interpolated steps.

For the example above you would expect the output.xyz to have 20 geometries of equidistant steps between the reactant and MECI.

NOTE: You need to do this TWICE, one is for the reactant -> a minimum energy conical intersection (MECI), and then another from MECI -> product 
