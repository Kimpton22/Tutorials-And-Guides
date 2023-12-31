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

# Step 2: Separation
Files that are needed: 
1. seperate.py - python script that will separate the xyz files from a combined xyz (i.e. output.xyz, wigner.300.xyz)

How to run: 
```
python3 separate.py {file_name.xyz} {output name}
```
Example: 
```
python3 separate.py output.xyz bd-td
```

Outputs: 
1. {output_name}[1-n].xyz - numbered xyz files containing the individual xyz from the interpolations, where n is the number of interpolated geometries

For the example above you would get a list of xyz files title bd-td-#.xyz, where # would be 1-20.

# Step 3: Alignment
Files that are needed:
1. overlay.py - python script that will align the geometries with a reference structure (put why this is important)
2. list.txt - text file that contains the filenames of the reference and interpolated geometries; you can generate the list with the following bash line:
   ```
   for ((a=1;a<={# of interpolated geometries};a++)); do echo {filename}-$a.xyz>> list.txt; done
   ```
4. reference.xyz - a reference xyz file with the original orientation (i.e. S0 optimized structure)

How to run:
```
python3 overlay.py list.txt
```

Outputs:
1. {filename}[1-n]-overlay.xyz - numbered xyz files that have been aligned with the original xyz file; where n is the number of the interpolated geometries

NOTE: Move all the overlay geometries into another folder (i.e. overlaid_geos) and use the following bash command to delete the '-overlay' from the file name. 
```
for i in *; do mv "$i" "${i%%-overlay.xyz}.xyz"; done
```

NOTE: You need to do this TWICE, one is for the reactant -> a minimum energy conical intersection (MECI), and then another from MECI -> product. 
