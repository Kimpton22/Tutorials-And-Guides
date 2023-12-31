# Case Study 1: Geodesic Interpolation
This step will generate the initial training data set for us to use with PyRAI2MD to conduct machine learning - non-adiabatic molecular dynamics. 

NOTE: You need to do the following steps TWICE, one is for the reactant -> a minimum energy conical intersection (MECI), and then another from MECI -> product. Each of these will have their folders. 

1. first_part -> contains the reactant -> MECI geometries
2. second_part -> contains the MECI -> product geometries

Lets start with the first_part folder (i.e. reactant -> MECI): 

# Step 1: Interpolation
Files that are needed: 
1. interpolation.sh - shell script that will run the geodesic interpolation.
2. point1-point2.xyz - an xyz file that contains 2 geometries; (1) reactant geometry (i.e. point 1) and (2) the product geometry (i.e. point 2). These are the two points where the geodesic interpolation will be done for.

How to run:
``` 
bash interpolation.sh {xyz file containing both geometries} {number of steps}
```

Example xyz file: 
```
INSERT XYZ FILE HERE
```

Example Command:
```
bash interpolation.sh reactant_meci.xyz 20
```

Outputs: 
1. output.xyz - a xyz file that contains all the interpolated steps.

For the example above you would expect the output.xyz to have 20 geometries of equidistant steps between the reactant and MECI.

# Step 2: Separation
Files that are needed: 
1. seperate.py - python script that will separate the xyz files from a combined xyz (i.e. output.xyz, wigner.300.xyz).

How to run: 
```
python3 separate.py {file_name.xyz} {output name}
```
Example: 
```
python3 separate.py output.xyz bd-td
```

Outputs: 
1. {output_name}[1-n].xyz - numbered xyz files containing the individual xyz from the interpolations, where n is the number of interpolated geometries.

For the example above you would get a list of xyz files title bd-td-#.xyz, where # would be 1-20.

# Step 3: Alignment
Files that are needed:
1. overlay.py - python script that will align the geometries with a reference structure.
2. list.txt - text file that contains the filenames of the reference and interpolated geometries; you can generate the list with the following bash line:
   ```
   for ((a=1;a<={# of interpolated geometries};a++)); do echo {filename}-$a.xyz>> list.txt; done
   ```
4. reference.xyz - a reference xyz file with the original orientation (i.e. S0 optimized structure).

How to run:
```
python3 overlay.py list.txt
```

Outputs:
1. {filename}[1-n]-overlay.xyz - numbered xyz files aligned with the original xyz file; where n is the number of the interpolated geometries.

For the example above you would expect an overlaid version of the 20 interpolated geometries.

NOTE: Move all the overlay geometries into another folder (i.e. overlaid_geos) and use the following bash command to delete the '-overlay' from the file name. 
```
for i in *; do mv "$i" "${i%%-overlay.xyz}.xyz"; done
```

# Step 4: Wigner Sampling
1. seperate.py - python scripts that separates the Wigner sampled geometries.
2. wigner-{filename}.300.0.xyz - an xyz file that contains all the geometries generated from the Wigner sampling.

How to run:
```
python3 seperate.py wigner-{filename}-300.0.xyz {output name}
```

Example: 
```
python3 seperate.py wigner-bd-td-300.0.xyz bd-td
```

Outputs: 
1. {output name}-[1-n].xyz - numbered xyz files for the individual Wigner sampled geometries.

For the example above you would expect to have the first n geometries of the Wigner sampling of the reactant.

# Step 5: Organization
This step is to organize the files to be able to set up single calculations for all the interpolated structures. 

Once you have complete steps 1-4 for both ```first_part``` (i.e. reactant -> MECI) and ```second_part``` (i.e. MECI -> product). 

1. Make directory title ```interpolation```
2. `cd interpolation`
3. Make directories for each part (i.e. `first_part` and `second_part`)
4. Copy the overlaid geometries into their respective folders
5. Move the directory that contains the Wigner sample geometries into the `interpolation` folder

# Step 6: Set-up Calculations
Files needed: 
1. Gen-wigner-interp.py - python script that generates the MOLCAS single-point calculations.
2. {filename}.inp - MOLCAS input file.
3. {filename}.StrOrb - MOLCAS starting orbitals, usually from the S0 optimized calculations.

How to run: 
```
python3 Gen-wigner-interp.py {filename}
```
Outputs: 
1. {filename}[1-n]/bd-td-[1-m] - folders containing the single point calculations, where n is the number of Wigner sample geometries and m is the number of interpolated steps.
2. runall.sh - shell script that will run all the calculations; usually split this due to hitting the limit of the job submission on the Discovery Cluster.




